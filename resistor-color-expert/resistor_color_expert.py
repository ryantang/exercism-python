VALUES = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,    
    'white': 9
    }

TOLERANCES = {
    'grey': '±0.05%',
    'violet': '±0.1%',
    'blue': '±0.25%',
    'green': '±0.5%',
    'brown': '±1%',
    'red': '±2%',
    'gold': '±5%',
    'silver': '±10%'
}

ONE_BILLIION = 10 ** 9
ONE_MILLION = 10 ** 6
ONE_THOUSAND = 10 ** 3


def resistor_label(colors):
    if len(colors) == 1:
        return '0 ohms'  #the only valid resister with a single band
    
    keys = colors.copy()
    tolerance_key = keys.pop()
    power_key = keys.pop()
    
    tolerance = TOLERANCES[tolerance_key]
    power = VALUES[power_key]

    # There are two or there keys remaining, representing the base value
    # If there are three, each color represents a digit in a three-digit number
    # Otherwise they represent a two-digit number
    # Example: ['brown','red','black'] => [1, 2, 3] => 123
    base_value = sum(
        VALUES[value_key] * (10 ** index)
        for index, value_key in enumerate(keys[::-1])
    )
    value = base_value * (10 ** power)
    
    return f'{_label(value, power)} {tolerance}'



def _label(value: int, power: int)-> str:

    if value == 0:
        return '0 ohms'
    if value % (ONE_BILLIION) == 0:
        return f'{value//(ONE_BILLIION)} gigaohms'
    if value >= (ONE_BILLIION):
        return f'{value/(ONE_BILLIION)} gigaohms'
    if value % (ONE_MILLION) == 0:
        return f'{value//(ONE_MILLION)} megaohms'
    if value >= (ONE_MILLION):
        return f'{value/(ONE_MILLION)} megaohms'
    if value % (ONE_THOUSAND) == 0:
        return f'{value//(ONE_THOUSAND)} kiloohms'
    if value >= (ONE_THOUSAND):
        return f'{value/(ONE_THOUSAND)} kiloohms'
    
    return f'{value} ohms' 