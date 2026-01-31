def line_up(name: str, number: int) -> str:
    """Generate a personalized customer message with ordinal number.
    
    Args:
        name: Customer's name
        number: Customer number (1, 2, 3, etc.)
    
    Returns:
        Personalized message like "Alice, you are the 1st customer we serve today. Thank you!"
    """
    return f"{name}, you are the {number}{_suffix(number)} customer we serve today. Thank you!"

def _suffix(number: int) -> str:
    """Return the ordinal suffix for a number (st, nd, rd, or th)."""
    num_str = str(number)

    last_two_digits = num_str[-2:]
    if last_two_digits in ("11", "12", "13"):
        return "th"

    last_digit = num_str[-1]
    match last_digit:
        case "1":
            return "st"
        case "2":
            return "nd"
        case "3":
            return "rd"
        case _:
            return "th"
