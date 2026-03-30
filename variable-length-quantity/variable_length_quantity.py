def encode(numbers):
    encoded_all = []
    for value in numbers:
        encoded = []
        if value == 0:
            encoded.append(0)

        while value:
            hex_digit = value % 128
            value = value // 128

            # Flip "continuation" bit for hex digits after the first hex digit.
            if encoded:
                hex_digit += 128
            encoded.append(hex_digit)

        encoded_all += list(reversed(encoded))

    return encoded_all


def decode(bytes_):
    decoded = []
    segment = []
    for place, hex_digit in enumerate(bytes_):
        if place == len(bytes_) - 1 and _continuation_bit_set(hex_digit):
            raise ValueError("incomplete sequence")

        if _continuation_bit_set(hex_digit):
            segment.append(hex_digit % 128)
        else:
            segment.append(hex_digit)
            decoded += _decode_segment(segment)
            segment = []

    if segment:
        decoded += _decode_segment(segment)

    return decoded

def _continuation_bit_set(hex_digit: int) -> bool:
    return bool(hex_digit // 128)

def _decode_segment(bytes_):
    decoded = 0
    for place, hex_value in enumerate(reversed(bytes_)):
        decoded += (hex_value % 128) * 128 ** place

    return [decoded]
