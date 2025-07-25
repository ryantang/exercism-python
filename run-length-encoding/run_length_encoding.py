def decode(string: str) -> str:
    if not string:
        return ''

    decoded_string = ''
    number_str = ''
    for char in string:
        if char.isdigit():
            number_str += char
        elif char.isalpha() or char.isspace():
            decoded_string += _expand(number_str, char)
            number_str = ''
        else:
            raise ValueError(f'Invalid character: {char}. Only digits, letters and whitespaces are allowed')

    return  decoded_string


def _expand(repeats: str, char) -> str:
    if repeats:
        return char * int(repeats)
    else:
        return char


def encode(string: str) -> str:
    if not string:
        return ''

    last = ''
    count = 0
    encoded_string = ''

    for char in string:
        if char != last:
            if last:
                encoded_string += _condense(count, last)
            last = char
            count = 1
        else:
            count += 1
    encoded_string += _condense(count, last)

    return encoded_string


def _condense(repeats: int, char: str) -> str:
    if repeats == 1:
        return char
    elif repeats > 1:
        return f'{repeats}{char}'
    else:
        raise ValueError(f'The number of repeats must be 1 or greater. Got {repeats}.')
