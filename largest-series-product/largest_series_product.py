import math

def largest_product(series: str, size: int) -> int:
    '''Given a multi-digit number, find the continugous digits 
    of the specified length with the largest product'''
    if size < 0:
        raise ValueError("span must not be negative")
    if size > len(series):
        raise ValueError("span must not exceed string length")
    if series and not series.isdigit():
        raise ValueError("digits input must only contain digits")

    largest = 0
    for span in _find_spans(series, size):
        largest = max(largest, math.prod(span))
    return largest


def _find_spans(series: str, size: int) -> list[int]:
    '''Yields spans of the given length'''
    digits = [int(digit) for digit in series]
    for starting_index in range(len(digits) + 1 - size):
        yield digits[starting_index:starting_index+size]
