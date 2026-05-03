import heapq
from collections import namedtuple
from typing import Iterator, TypeAlias, Callable


FactorPairs: TypeAlias = set[tuple[int,int]]
Product = namedtuple('Product', ['value', 'factor1', 'factor2'])
INCREASING = 1
DECREASING = -1


def largest(min_factor: int, max_factor: int) -> tuple[int|None, FactorPairs]:
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError('min must be <= max')

    for product in _products_decreasing(min_factor, max_factor):
        if _is_palindrome(product.value):
            answer = (product.value, _factors(product.value, min_factor, max_factor))
            return answer

    return (None, [])

def smallest(min_factor: int, max_factor: int) -> tuple[int|None, FactorPairs]:
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError('min must be <= max')


    for product in _products_increasing(min_factor, max_factor):
        if _is_palindrome(product.value):
            answer = (product.value, _factors(product.value, min_factor, max_factor))
            return answer

    return (None, [])

def _factors(product: Product, min_factor: int, max_factor: int) -> FactorPairs:
    """Find all factor pairs of a product within a given range."""
    factors = set()
    for factor in range(min_factor, max_factor + 1):
        if product % factor == 0 and min_factor <= product//factor <= max_factor:
            factors.add(tuple(sorted((factor, product//factor))))

    return factors

def _is_palindrome(product: Product) -> bool:
    """Check if a number is a palindrome."""
    return product == int(str(product)[::-1])

def _products_increasing(min_factor: int, max_factor: int) -> Iterator[Product]:
    """Generate products in increasing order, starting from the smallest."""
    return _products_generator(
        initial_product=_square_of(min_factor),
        min_factor=min_factor,
        max_factor=max_factor,
        direction=INCREASING,
        push_func=heapq.heappush,
        pop_func=heapq.heappop
    )

def _products_decreasing(min_factor: int, max_factor: int) -> Iterator[Product]:
    """Generate products in decreasing order, starting from the largest."""

    return _products_generator(
        initial_product=_square_of(max_factor),
        min_factor=min_factor,
        max_factor=max_factor,
        direction=DECREASING,
        push_func=heapq.heappush_max,
        pop_func=heapq.heappop_max
    )


def _products_generator(
        initial_product: Product,
        min_factor: int,
        max_factor: int,
        direction: int,
        push_func: Callable[list, Product],
        pop_func: Callable[list, Product],
    ) -> Iterator[Product]:
    """
    This function implements a search algorithm that efficiently finds the
    next smallest (or largest) product at each step.

    Example with direction=INCREASING: In this case, the caller passes in the
    smallest possible value as the initial_product. It keeps track of the
    "seen" values in a set and the upcoming next smallest values in a min_heap
    list called "products". After popping off the next smallest product from
    "products", this function searches for its next incrementally larger neighbors
    ensures that they're valid cadidates and adds them to the "products" heap.

    This works the same way with direction=DECREASING, but reversed and uses
    max_heap instead of a min_heap.
    """
    products = [initial_product]
    seen_values = {initial_product.value}

    while products:
        product = pop_func(products)
        yield product

        for next_product in _next_products(product, direction):
            if next_product.value in seen_values:
                continue
            if not _within_bounds(next_product, min_factor, max_factor):
                continue

            seen_values.add(next_product.value)
            push_func(products, next_product)



def _square_of(factor: int) -> Product:
    """Calculate the square of a factor."""
    return Product(
        value = factor * factor,
        factor1 = factor,
        factor2 = factor
    )

def _next_products(product: Product, direction: int) -> tuple[Product]:
    """Calculate the next two candidate products in the search grid."""
    next_in_row = Product(
        value = product.factor1 * (product.factor2 + direction),
        factor1 = product.factor1,
        factor2 = product.factor2 + direction
    )

    next_in_col = Product(
        value = (product.factor1 + direction) * product.factor2,
        factor1 = product.factor1 + direction,
        factor2 = product.factor2
    )

    return (next_in_row, next_in_col)

def _within_bounds(product: Product, min_factor: int, max_factor: int) -> bool:
    """Check if a product's factors are within the allowed range."""
    return (min_factor <= product.factor1 <= max_factor
            and min_factor <= product.factor2 <= max_factor)
