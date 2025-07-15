import string

ENCODE_TABLE = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])

def encode(plain_text):
    cleaning_table = str.maketrans('','',string.punctuation + ' ')
    cleaned_text = plain_text.translate(cleaning_table).lower()

    encoded = cleaned_text.translate(ENCODE_TABLE)

    encoded_with_spaces = ' '.join(
        encoded[index: index + 5]
        for index in range(0, len(encoded), 5)
    )

    return encoded_with_spaces


def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(' ','').lower()
    return ciphered_text.translate(ENCODE_TABLE)