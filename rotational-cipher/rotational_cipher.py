from string import ascii_lowercase, ascii_uppercase

def rotate(text: str, key: int) -> str:
    """Performs a rotational cipher on a string

    Args:
        text: str - the text to rotate or "encrypt"
        key: int - the number of letters to rotate

    Reuturns:
        str: Rotated or "encrypted" string

    Example: 
        rotate('xyz', 1) returns 'yza', which rotates each letter forward by one.  z cycles around to a.
    """
    rotator = _create_rotator_map(key)

    return ''.join(
        rotator.get(character, character)
        for character in text
    )

def _create_rotator_map(key):
    rotated_lowercase = ascii_lowercase[key:] + ascii_lowercase[:key]
    rotated_uppercase = ascii_uppercase[key:] + ascii_uppercase[:key]

    lowercase_map = dict(zip(ascii_lowercase, rotated_lowercase))
    uppercase_map = dict(zip(ascii_uppercase, rotated_uppercase))

    return lowercase_map | uppercase_map

