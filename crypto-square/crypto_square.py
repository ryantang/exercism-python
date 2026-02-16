import math


def cipher_text(plain_text: str) -> str:
    """Encode a string using the square code cipher.
    
    Normalizes input, arranges into a rectangle based on length,
    transposes the matrix, and returns columns separated by spaces.
    """
    normalized = _normalize(plain_text)
    if not normalized:
        return normalized

    # Calculate rectangle dimensions: as "square" as possible
    num_cols = math.ceil(math.sqrt(len(normalized)))
    num_rows = math.ceil(len(normalized) / num_cols)
    padded_text = normalized.ljust(num_cols * num_rows)

    # Build matrix by splitting normalized text into rows
    matrix = [
        list(padded_text[i * num_cols:(i + 1) * num_cols])
        for i in range(num_rows)
    ]

    # Transpose matrix and join columns with spaces
    transposed = ["".join(row) for row in zip(*matrix)]
    return ' '.join(transposed)


def _normalize(text: str) -> str:
    """Remove non-alphanumeric characters and convert to lowercase."""
    return ''.join(char for char in text.lower() if char.isalnum())
