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
        raise ValueError('min must be <= max')

    for product in _products(DECREASING, min_factor, max_factor):
        if _is_palindrome(product.value):
            answer = (product.value, _factors(product.value, min_factor, max_factor))
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
        raise ValueError('min must be <= max')


    for product in _products(INCREASING, min_factor, max_factor):
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

def _products(direction, min_factor, max_factor):
    if direction == INCREASING:
        product = _product_with(min_factor)
    elif direction == DECREASING:
        product = _product_with(max_factor)
    else:
        raise ValueError('direction must be INCREASING (1) or DECREASING (-1)')

    seen = {product.value}
    products = [product]

    while products:
        if direction == INCREASING:
            product = heapq.heappop(products)
        elif direction == DECREASING:
            products.sort(key=lambda p: p.value)
            product = products.pop()
        yield product

        horizontal_neighbor = _horizontal_neighbor(product, max_factor, direction)
        if horizontal_neighbor and not horizontal_neighbor.value in seen:
            seen.add(horizontal_neighbor.value)
            if direction == INCREASING:
                heapq.heappush(products, horizontal_neighbor)
            else:
                products.append(horizontal_neighbor)

        vertical_neighbor = _vertical_neighbor(product, min_factor, direction)
        if vertical_neighbor and not vertical_neighbor.value in seen:
            seen.add(vertical_neighbor.value)
            if direction == INCREASING:
                heapq.heappush(products, vertical_neighbor)
            else:
                products.append(vertical_neighbor)

def _product_with(factor):
    return Product (value=factor*factor, factor1=factor, factor2=factor)

def _horizontal_neighbor(previous, max_factor, direction):
    if direction == INCREASING and previous.factor2 >= max_factor:
        return None
    if direction == DECREASING and previous.factor1 >= previous.factor2:
        return None

    return Product(
        value = previous.factor1 * (previous.factor2 + direction), 
        factor1 = previous.factor1, 
        factor2 = previous.factor2 + direction
        )

def _vertical_neighbor(previous, min_factor, direction):
    if direction == DECREASING and previous.factor1 <= min_factor:
        return None
    if direction == INCREASING and previous.factor1 >= previous.factor2:
        return None

    return Product(
        value = (previous.factor1 + direction) * previous.factor2,
        factor1 = previous.factor1 + direction,
        factor2 = previous.factor2
    )
