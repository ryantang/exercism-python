def convert(number: int) -> str:
    """Convert a number into a string with raindrop sounds.
    
    Args:
        number: The number to convert
        
    Returns:
        str: A string of raindrop sounds based on the number's factors:
            - If number has 3 as factor, adds 'Pling'
            - If number has 5 as factor, adds 'Plang'
            - If number has 7 as factor, adds 'Plong'
            - If number has none of these factors, returns the number as string
            
    Example:
        >>> convert(28)
        'Plong'
        >>> convert(30)
        'PlingPlang'
        >>> convert(34)
        '34'
    """
    result = ""

    if number % 3 == 0:
        result += ("Pling")
    if number % 5 == 0:
        result += ("Plang")
    if number % 7 == 0:
        result += ("Plong")
    if result:
        return result
    else:
        return str(number)
