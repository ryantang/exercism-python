from collections import deque
UP = 1
DOWN = -1


def encode(message: str, rails: int) -> str:
    """Encode a message using the rail fence cipher."""
    rail_index = _generate_rail_index(rails, len(message))
    by_rail = [[] for _ in range(rails)]

    for char_index, char in enumerate(message):
        by_rail[rail_index[char_index]].append(char)

    return ''.join(''.join(row) for row in by_rail)


def decode(encoded_message: str, rails: int) -> str:
    """Decode a message using the rail fence cipher."""
    length = len(encoded_message)
    rail_indices = _generate_rail_index(rails, length)
    chars_per_rail = _calculate_chars_per_rail(length, rails)

    rails_content = [None] * rails
    for rail_index in range(rails):
        start = sum(chars_per_rail[prev_rail_index] for prev_rail_index in range(rail_index))
        end = start + chars_per_rail[rail_index]
        rails_content[rail_index] = deque(encoded_message[start:end])

    message = (
        rails_content[rail_index].popleft()
        for rail_index in rail_indices
    )

    return ''.join(message)

def _calculate_chars_per_rail(message_length: int, rails:int) -> list[int]:
    """Calculate how many characters belong to each rail."""
    cycle_len = 2 * (rails - 1)
    full_cycles = message_length // cycle_len
    remaining_chars = message_length % cycle_len

    chars_per_rail = [
        _base_chars(full_cycles, rail, rails) + _extra_chars(remaining_chars, rail, rails)
        for rail in range(rails)
    ]

    return chars_per_rail

def _extra_chars(remaining_chars: int, rail: int, rails: int) -> int:
    """Calculate extra characters for a rail from the incomplete final cycle."""
    last_rail = rails - 1
    steps_up_from_last_rail = last_rail - rail

    if remaining_chars <= rail:
        return 0
    if remaining_chars > last_rail + steps_up_from_last_rail:
        return 2
    return 1


def _base_chars(full_cycles: int, rail: int, rails: int) -> int:
    """Calculate the base number of characters for a rail from full cycles."""
    if rail == 0 or rail == rails -1:
        return full_cycles
    return 2 * full_cycles


def _generate_rail_index(rails: int, message_length: int) -> list[int]:
    """Generate the sequence of rail indices for the zigzag pattern."""
    if rails < 0:
        raise ValueError('rails must be greater than or equal to 1')
    if rails == 1:
        return [0] * message_length

    direction = UP
    rail_indices = [None] * message_length
    rail_indices[0] = 0

    for char_index in range(1, message_length):
        previous_rail = rail_indices[char_index - 1]
        if previous_rail == 0:
            direction = UP
        elif previous_rail == rails - 1:
            direction = DOWN

        rail_indices[char_index] = previous_rail + direction

    return rail_indices
