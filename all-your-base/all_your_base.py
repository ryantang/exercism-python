def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(digit < 0 or digit >= input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")


    base_ten_value = _convert_to_base_ten(input_base, digits)
    return _convert_from_base_ten(output_base, base_ten_value)


def _convert_from_base_ten(output_base, base_ten_value):
    if not base_ten_value:
        return [0]

    converted_value = []
    working_value = base_ten_value
    while working_value:
        converted_value.append(working_value % output_base)
        working_value = working_value // output_base

    return list(reversed(converted_value))


def _convert_to_base_ten(input_base, digits):
    return sum(
        digit * (input_base ** place)
        for place, digit in enumerate(reversed(digits))
    )
