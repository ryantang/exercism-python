NUMBERS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

def say(number: int, chunks: list[int] = None) -> str:
    """Convert a number to its English representation.
    
    This function recursively breaks down a number into groups of three digits
    and converts each group into words, adding the appropriate scale suffix
    (thousand, million, billion).
    
    Args:
        number: The integer to convert to words
        chunks: Internal parameter used for recursion tracking digit groups
        
    Returns:
        String representation of the number in English words
        
    Raises:
        ValueError: If number is negative or exceeds 999,999,999,999
        
    Examples:
        >>> say(0)
        'zero'
        >>> say(123)
        'one hundred twenty-three'
        >>> say(1234)
        'one thousand two hundred thirty-four'
    """
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"
    
    # prevents test pollution, otherwise chunks persist across tests
    if chunks == None: 
        chunks = [] 

    # recursive base case
    if number < 1000:
        chunks.append(number)
        return _build(chunks)

    quotient, remainder = divmod(number, 1000)
    chunks.append(remainder)
    return say(quotient, chunks)

def _build(chunks: list[int]) -> str:
    """Convert chunks of 3-digit numbers into a full English phrase.
    
    Args:
        chunks: List of 3-digit numbers, ordered from least to most significant
        
    Returns:
        Full English representation with appropriate scale words
    """
    places = ["", " thousand", " million", " billion"]

    words = [
        f'{_three_digits(num)}{places[i]}'
        for i, num in enumerate(chunks)
        if num != 0
    ]
    print(f'words is {words}')

    return " ".join(words[::-1])


def _three_digits(num: int) -> str:
    """Convert a number from 0-999 to English words.
    
    Args:
        num: Number between 0-999 to convert
        
    Returns:
        English representation of the number
    """
    hundreds, remainder = divmod(num, 100)

    if hundreds:
        hundreds_word = f'{NUMBERS[hundreds]} hundred'

        if remainder:
            return f'{hundreds_word} {_two_digits(remainder)}'

        return hundreds_word

    return _two_digits(remainder)

    
def _two_digits(num: int) -> str:
    """Convert a number from 0-99 to English words.
    
    Args:
        num: Number between 0-99 to convert
        
    Returns:
        English representation of the number
    """
    if num < 20 or num % 10 == 0:
        return NUMBERS[num]

    tens, ones = divmod(num, 10)
    return f'{NUMBERS[tens * 10]}-{NUMBERS[ones]}'