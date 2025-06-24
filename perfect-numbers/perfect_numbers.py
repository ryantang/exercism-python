def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')

    factors_excluding_self = (
        factor for factor in range(1, number//2 + 1) #optimization: there no factors for N between N/2 and N.
        if number % factor == 0
    )

    total = sum(factors_excluding_self)

    if total == number:
        return 'perfect'
    if total > number:
        return 'abundant'
    
    # if total < number:
    return 'deficient'
