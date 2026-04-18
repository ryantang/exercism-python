from collections import deque
UP = 1
DOWN = -1

def encode(message, rails):
    rail_index = _generate_rail_index(rails, len(message))
    by_rail = [[] for _ in range(rails)]

    for char_index, char in enumerate(message):
        by_rail[rail_index[char_index]].append(char)

    return ''.join(''.join(row) for row in by_rail)



def decode(encoded_message, rails):
    length = len(encoded_message)
    rail_num = _generate_rail_index(rails, length)
    by_rail = [None for _ in range(rails)]

    k = length//(2 * (rails - 1))
    remainder = length - (2 * k * (rails - 1))
    rail_length=[None] * rails

    for i in range(rails):
        if i in (0, rails - 1): #top or bottom rail
            base = k
            extra = 1 if remainder > i else 0
        else: #middle rail
            base = 2 * k
            extra = 0
            if remainder > i:
                extra += 1
            if remainder > (rails - 1 + (rails - 1 - i)):
                extra +=1

        rail_length[i] = base + extra

    print(f'rail_length is {rail_length}')

    by_rail = [None] * rails
    for i in range(rails):
        if i == 0:
            by_rail[i] = deque(encoded_message[:rail_length[i]])
        else:
            start = sum(rail_length[j] for j in range(i))
            end = start + rail_length[i]
            by_rail[i] = deque(encoded_message[start:end])

    print(f'by_rail is {by_rail}')

    message = []

    for rail in rail_num:
        message.append(by_rail[rail].popleft())

    return ''.join(message)


def _generate_rail_index(rails, count):
    if rails < 0:
        raise ValueError("rails must be greater than or equal to 1")
    if rails == 1:
        return [0] * count

    direction = UP
    rail_indices = [None] * count
    rail_indices[0] = 0

    for i in range(1, count):
        previous_rail = rail_indices[i -1]
        if previous_rail == 0:
            direction = UP
        elif previous_rail == rails - 1:
            direction = DOWN

        rail_indices[i] = previous_rail + direction

    return rail_indices
