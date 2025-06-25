def is_isogram(phrase: str) -> bool:
    """Determines whether a phrase is an isogram (has no repeating letters)

    Arg:
        phrase: str - string to test whether it's an isogram
    
    Returns:
        bool: True if it's an isogram, False if not

    """
    letters = [char.lower() for char in phrase if char.isalpha()]
    unique_letters = set(letters)
    return len(letters) == len(unique_letters)