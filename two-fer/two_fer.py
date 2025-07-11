def two_fer(name: str ='you') -> str:
    """Generate a two fer statement wtih the name passed in
    
    Args:
        name (str, optional): The name to include in the phrase. Defaults to 'you'.

    Returns:
        str: A string in the format "One for {name}, one for me."
    
    Examples:
        >>> two_fer()
        'One for you, one for me.'
        >>> two_fer('Juliet')
        'One for Juliet, one for me.'

    """
    return f'One for {name}, one for me.'
