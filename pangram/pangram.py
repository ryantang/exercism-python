from string import ascii_lowercase
ALPHABET = set(ascii_lowercase)

def is_pangram(sentence):
    return ALPHABET.issubset(sentence.lower())
