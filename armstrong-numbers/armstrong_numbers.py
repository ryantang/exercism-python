def is_armstrong_number(number) -> bool:
    """Determine if an integer is an Armstrong number.
    An Armstrong number is number that is the sum of its own
    digits raised to the power of the number of digits.

    Args:
        number: integer to check
    
    Returns:
        bool: True if the number is an Armstrong number, False if not

    Example:
    >>> is_armstrong_number(153)  # 1^3 + 5^3 + 3^3 = 153
    True
    >>> is_armstrong_number(154)
    False

    """
    digits = [int(digit) for digit in str(number)]
    power = len(digits)    
    return number == sum(digit ** power for digit in digits)