from collections import deque

def encode(numbers: list[int]) -> list[int]:
    """Encodes a list of numbers into a variable-length quantity."""
    encoded_all = []
    for value in numbers:
        encoded = deque()
        if value == 0:
            encoded.append(0)

        while value:
            hex_digit = value % 128
            value = value // 128

            # Set "continuation" bit for hex digits after the first hex digit.
            if encoded:
                hex_digit += 128
            encoded.appendleft(hex_digit)

        encoded_all += encoded

    return encoded_all


def decode(bytes_: list[int]) -> list[int]:
    """Decodes a variable-length quantity into a list of numbers."""
    if not bytes_ or _continuation_bit_set(bytes_[-1]):
        raise ValueError("incomplete sequence")

    decoded = []
    segment = []
    for hex_digit in bytes_:
        if _continuation_bit_set(hex_digit):
            segment.append(hex_digit % 128)
        else:
            segment.append(hex_digit)
            decoded.append(_decode_segment(segment))
            segment = []

    return decoded

def _continuation_bit_set(hex_digit: int) -> bool:
    """Checks if the continuation bit is set for a given byte."""
    return bool(hex_digit // 128)

def _decode_segment(bytes_: list[int]) -> int:
    """Decodes a single variable-length number segment."""
    decoded = 0
    for place, hex_value in enumerate(reversed(bytes_)):
        decoded += (hex_value % 128) * 128 ** place

    return decoded
