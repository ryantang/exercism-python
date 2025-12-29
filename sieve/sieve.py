import math

def primes(limit: int) -> list[int]:
    """Find primes up to a limit using the Sieve of Eratosthenes algorithm

    Args:
        limit (int): The upper bound.

    Returns:
        list: The resulting prime.
    """
    prime_by_index = [True] * (limit + 1)
    _set_zero_and_one_not_prime(prime_by_index)

    for index in range(2, math.floor(math.sqrt(limit)) + 1):
        if prime_by_index[index]:
            # Skip composites; their multiples were already marked by smaller primes
            for multiple in range(index * 2, limit + 1, index):
                prime_by_index[multiple] = False

    return [index for index, is_prime in enumerate(prime_by_index) if is_prime]

def _set_zero_and_one_not_prime(primes_list) -> None:
    primes_list[0] = primes_list[1] = False
