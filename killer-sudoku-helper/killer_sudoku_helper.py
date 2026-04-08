import itertools

NUMBERS = set(range(1,10))

def combinations(target: int, size: int, exclude: list[int]) -> list[list[int]]:
    """
    Finds combinations of numbers that sum to a target,
    given a size and a list of numbers to exclude.
    """
    valid_numbers = NUMBERS - set(exclude)
    return [
        list(combo)
        for combo in itertools.combinations(valid_numbers, size)
        if sum(combo) == target
    ]
