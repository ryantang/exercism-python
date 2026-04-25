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
        if _is_palindrome(product):
            answer = (product, _factors(product, min_factor, max_factor))
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
        if _is_palindrome(product):
            answer = (product, _factors(product, min_factor, max_factor))
            print(f"answer is {answer}")
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
    products = []
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1):
            products.append(i * j)
    
    return sorted(products)


def _products_decreasing(min_factor, max_factor):
    products = []
    for i in range(max_factor, min_factor - 1, -1):
        for j in range(max_factor, min_factor - 1, -1):
            products.append(i * j)

    return sorted(products, reverse=True)

