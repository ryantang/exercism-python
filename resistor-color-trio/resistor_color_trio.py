COLORS = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9,
    }

def label(colors: list[str]) -> str:
    """ Determine the value of a resister based on colored bands

    Args:
        colors: List of strings representing the color bands

    Returns:
        str: Resistance value with units
    """
    first, second, third, *_ = colors

    power = COLORS[third]
    value = (COLORS[first] * 10 + COLORS[second]) * (10 ** power)
    unit_modifier = ''

    if value == 0:
        return '0 ohms'
    if value % (10 ** 9) == 0:
        return f'{value//(10 ** 9)} gigaohms'
    elif value % (10 ** 6) == 0:
        return f'{value//(10 ** 6)} megaohms'
    elif value % (10 ** 3) == 0:
        return f'{value//(10 ** 3)} kiloohms'
    
    return f'{value} {unit_modifier}ohms' 
