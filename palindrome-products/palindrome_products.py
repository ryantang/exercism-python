from collections import namedtuple

Product = namedtuple('Product', ['value', 'factor1', 'factor2'])

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
    lowest_product = Product(value=min_factor*min_factor,factor1=min_factor, factor2=min_factor)
    products = [lowest_product]
    while products:
        products.sort(key=lambda p: p.value, reverse=True)
        product = products.pop()
        print(f'product is {product}')
        yield product

        if product.factor2 < max_factor:
            right_factor1 = product.factor1
            right_factor2 = product.factor2 + 1
            right_product_val = right_factor1 * right_factor2
            print(f'right_product_val is {right_product_val}')

            if not any(p.value == right_product_val for p in products):
                right_product = Product(value=right_product_val,factor1=right_factor1,factor2=right_factor2)
                products.append(right_product)
        if product.factor1 < product.factor2:
            up_factor1 = product.factor1 + 1
            up_factor2 = product.factor2
            up_product_val = up_factor1 * up_factor2
            if not any(p.value == up_product_val for p in products):
                up_product = Product(value=up_product_val, factor1=up_factor1, factor2=up_factor2)
                products.append(up_product)


def _products_decreasing(min_factor, max_factor):
    highest_product = Product(value=max_factor*max_factor,factor1=max_factor, factor2=max_factor)
    products = [highest_product]
    while products:
        products.sort(key=lambda p: p.value)
        product = products.pop()
        print(f'product is {product}')
        yield product

        if product.factor2 > min_factor:
            down_factor1 = product.factor1
            down_factor2 = product.factor2 - 1
            down_product_val = down_factor1 * down_factor2
            if not any(p.value == down_product_val for p in products):
                down_product = Product(value=down_product_val,factor1=down_factor1,factor2=down_factor2)
                products.append(down_product)

        if product.factor1 > product.factor2:
            left_factor1 = product.factor1 - 1
            left_factor2 = product.factor2
            left_product_val = left_factor1 * left_factor2
            if not any(p.value == left_product_val for p in products):
                left_product = Product(value=left_product_val, factor1=left_factor1, factor2=left_factor2)
                products.append(left_product)
