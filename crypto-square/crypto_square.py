import math
import copy

def cipher_text(plain_text):
    normalized = _normalize(plain_text)
    print(f"normalized text is {normalized}")

    len_normalized = len(normalized)
    num_cols = math.ceil(math.sqrt(len_normalized))
    if num_cols * (num_cols - 1) >= len_normalized:
        num_rows = num_cols - 1
    else:
        num_rows = num_cols

    padding_length = num_cols * num_rows - len_normalized
    normalized = normalized + " " * padding_length

    matrix = []

    for i in range(num_rows):
        start = i * num_cols
        end = start + num_cols
        row = list(normalized[start:end])
        matrix.append(row)

    transposed = ["".join(row) for row in zip(*matrix)]
    return ' '.join(transposed)


def _normalize(text):
    return ''.join(char for char in str.lower(text) if str.isalnum(char))
