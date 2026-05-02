import heapq
from collections import namedtuple

Product = namedtuple('Product', ['value', 'factor1', 'factor2'])
INCREASING = 1
DECREASING = -1

def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    for product in _products_decreasing(min_factor, max_factor):
        if _is_palindrome(product.value):
            answer = (product.value, _factors(product.value, min_factor, max_factor))
            print(f"answer is {answer}")
            return answer

    return [None, []]

def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")


    for product in _products_increasing(min_factor, max_factor):
        if _is_palindrome(product.value):
            answer = (product.value, _factors(product.value, min_factor, max_factor))
            return answer

    return [None, []]

def _factors(product, min_factor, max_factor):
    factors = set()
    for factor in range(min_factor, max_factor + 1):
        if product % factor == 0 and min_factor <= product//factor <= max_factor:
            factors.add(tuple(sorted((factor, product//factor))))

    return factors

def _is_palindrome(product):
    return product == int(str(product)[::-1])

def _products_increasing(min_factor, max_factor):
    lowest_product = _lowest_product(min_factor)
    products = [lowest_product]
    seen_values = {lowest_product.value}

    while products:
        product = heapq.heappop(products)
        yield product

        for next_product in _next_products(product, INCREASING):
            if next_product.value in seen_values:
                continue
            if not _within_bounds(next_product, min_factor, max_factor):
                continue

            seen_values.add(next_product.value)
            heapq.heappush(products, next_product)


def _products_decreasing(min_factor, max_factor):
    highest_product = _highest_product(max_factor)
    products = [highest_product]
    seen_values = {highest_product.value}

    while products:
        products.sort(key=lambda p: p.value)
        product = products.pop()
        yield product

        for next_product in _next_products(product, DECREASING):
            if next_product.value in seen_values:
                continue
            if not _within_bounds(next_product, min_factor, max_factor):
                continue

            seen_values.add(next_product.value)
            products.append(next_product)

def _lowest_product(min_factor):
    return Product(
        value = min_factor * min_factor,
        factor1 = min_factor,
        factor2 = min_factor
    )

def _highest_product(max_factor):
    return Product(
        value = max_factor * max_factor,
        factor1 = max_factor,
        factor2=max_factor
    )

def _next_products(product, direction):
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

def _within_bounds(product, min_factor, max_factor):
    return (min_factor <= product.factor1 <= max_factor
            and min_factor <= product.factor2 <= max_factor)