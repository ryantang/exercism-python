from functools import reduce

def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """Convert digits from input_base to output_base."""
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(digit < 0 or digit >= input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    base_ten_value = _convert_to_base_ten(input_base, digits)
    return _convert_from_base_ten(output_base, base_ten_value)


def _convert_from_base_ten(output_base: int, base_ten_value: int) -> list[int]:
    """Convert a base-10 integer to a list of digits in output_base."""
    if base_ten_value == 0:
        return [0]

    converted_value = []
    while base_ten_value:
        base_ten_value, remainder = divmod(base_ten_value, output_base)
        converted_value.append(remainder)

    return converted_value[::-1]


def _convert_to_base_ten(input_base: int, digits: list[int]) -> int:
    """Convert a list of digits in input_base to a base-10 integer."""
    value = 0
    for digit in digits:
        value = value * input_base + digit

    return value
