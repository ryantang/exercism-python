from collections import deque
SEVEN_BIT_BASE = 128
CONTINUATION_BIT = 128

def encode(numbers: list[int]) -> list[int]:
    """Encodes a list of numbers into a variable-length quantity."""
    encoded_all = []
    for number in numbers:
        encoded = deque()
        remaining_value = number

        if remaining_value == 0:
            encoded.append(0)

        while remaining_value:
            hex_digit = remaining_value % SEVEN_BIT_BASE
            remaining_value = remaining_value // SEVEN_BIT_BASE

            # Set "continuation" bit for hex digits after the first hex digit.
            if encoded:
                hex_digit += CONTINUATION_BIT
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
            segment.append(hex_digit % CONTINUATION_BIT)
        else:
            segment.append(hex_digit)
            decoded.append(_decode_segment(segment))
            segment = []

    return decoded

def _continuation_bit_set(hex_digit: int) -> bool:
    """Checks if the continuation bit is set for a given byte."""
    return bool(hex_digit // CONTINUATION_BIT)

def _decode_segment(bytes_: list[int]) -> int:
    """Decodes a single variable-length number segment."""
    decoded = 0
    for place, hex_value in enumerate(reversed(bytes_)):
        decoded += (hex_value % SEVEN_BIT_BASE) * SEVEN_BIT_BASE ** place

    return decoded
