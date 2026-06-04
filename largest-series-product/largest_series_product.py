import math

def largest_product(series, size):
    if size < 0:
        raise ValueError("span must not be negative")
    if size > len(series):
        raise ValueError("span must not exceed string length")
    try:
        int(series)
    except Exception as e:
        raise ValueError("digits input must only contain digits") from e


    largest = 0
    for span in _find_spans(series, size):
        largest = max(largest, math.prod(span))
    return largest


def _find_spans(series, size):
    digits = [int(digit) for digit in series]
    for starting_index in range(len(digits) + 1 - size):
        yield digits[starting_index:starting_index+size]
