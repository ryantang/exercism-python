import string

def abbreviate(words):
    punctuation_minus_dash = string.punctuation.replace('-', '')

    cleaned = ''.join(
        char
        for char in words
        if char not in punctuation_minus_dash
    )

    separators = [
        i
        for i, char in enumerate(cleaned)
        if char in [' ', '-']
    ]

    first_letter = cleaned[0].upper()

    letters = [
        cleaned[i+1].upper()
        for i in separators
        if cleaned[i+1].isalpha()
    ]

    return ''.join([first_letter] + letters)
