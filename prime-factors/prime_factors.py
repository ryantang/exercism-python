from math import sqrt

def factors(value, factor_list=[]):
    if value == 1:
        return factor_list
    
    new_factor = _smallest_prime_factor(value)
    return factors(value // new_factor, factor_list + [new_factor])

def _smallest_prime_factor(value):
    for x in range(2, int(sqrt(value)) + 1):
        if value % x == 0:
            return x
    
    return value