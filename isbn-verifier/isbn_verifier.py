ISBN_LENGTH = 10


def is_valid(isbn: str) -> bool:
    """Determine if a string is a valid ISBN-10.
    
    Args:
        isbn: String to validate as ISBN-10
        
    Returns:
        bool: True if string is valid ISBN-10, False otherwise
        
    Example:
        >>> is_valid("3-598-21508-8")
        True
        >>> is_valid("3-598-21508-9")
        False
    """
    cleaned_isbn = list(isbn.replace('-', ''))
    if len(cleaned_isbn) != ISBN_LENGTH:
        return False

    if cleaned_isbn[-1] == 'X':
        cleaned_isbn[-1] = '10'

    if not all(digit.isdigit() for digit in cleaned_isbn):
        return False
    
    weighted_sum = sum(
        int(digit) * (10 - index)
        for index, digit in enumerate(cleaned_isbn)
    )

    return weighted_sum % 11 == 0