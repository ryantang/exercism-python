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

    cleaned_isbn = isbn.replace('-','')
    if len(cleaned_isbn) != ISBN_LENGTH:
        return False

    digits = cleaned_isbn[:9]
    checksum = cleaned_isbn[-1]

    if not digits.isdigit():
        return False
    
    if not _valid_checksum(checksum):
        return False

    return (_weighted_sum(digits) + _checksum_value(checksum)) % 11 == 0

def _valid_checksum(checksum: str) -> bool:
    return checksum.isdigit() or checksum == 'X'

def _weighted_sum(digits: str) -> bool:
    return sum(
        int(digit) * (10 - index)
        for index, digit in enumerate(digits)
    )

def _checksum_value(checksum: str) -> bool:
    return (10 if checksum == 'X' else int(checksum))