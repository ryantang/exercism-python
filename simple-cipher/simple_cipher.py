import string
import secrets

class Cipher:
    ALPHABET = string.ascii_lowercase
    ALPHABET_SIZE = len(ALPHABET)
    ROTATION_MAP = dict(zip(ALPHABET, range(ALPHABET_SIZE)))

    def __init__(self, key=None) -> None:
        if key:
            self._key = key
        else:
            random_letters = [secrets.choice(self.ALPHABET) for _ in range(100)]
            self._key = "".join(random_letters)

        self._rotate_by = [self.ROTATION_MAP[char] for char in self._key]

    def encode(self, text: str) -> str:
        return self._transform(text, 1)


    def decode(self, text: str) -> str:
        return self._transform(text, -1)


    def _transform(self, text: str, direction: int) -> str:
        plaintext_chars = []
        for i, char in enumerate(text):
            az_pos = self.ROTATION_MAP[char]
            cipher_char_index =  az_pos + direction * self._rotate_by[i % len(self._key)]
            plaintext_chars += self.ALPHABET[cipher_char_index % self.ALPHABET_SIZE]

        return "".join(plaintext_chars)


    @property
    def key(self) -> str:
        return self._key
