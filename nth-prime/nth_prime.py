import math

def prime(number):
    if number == 0:
        raise ValueError("there is no zeroth prime")

    primes = []
    current_num = 2

    while len(primes) < number:
        if _is_prime(current_num):
            primes.append(current_num)

        current_num += 1

    return primes[-1]


def _is_prime(num: int) -> bool:
    max = int(math.sqrt(num)) + 1

    for i in range(2, max):
        if num % i == 0:
            return False
        
    return True
