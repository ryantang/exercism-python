from collections import deque
UP = 1
DOWN = -1

def encode(message, rails):
    rail_num = _zigzag(rails, len(message))
    by_rail = [[] for _ in range(rails)]

    for index, char in enumerate(message):
        by_rail[rail_num[index]- 1].append(char)

    return ''.join([
        ''.join(row)
        for row in by_rail
    ])



def decode(encoded_message, rails):
    length = len(encoded_message)
    rail_num = _zigzag(rails, length)
    by_rail = [None for _ in range(rails)]

    k = length//(2 * (rails - 1))
    remainder = length - (2 * k * (rails - 1))
    print(f'k and length is {k} and {length}')
    print(f'remainder is {remainder}')

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
        message.append(by_rail[rail - 1].popleft())

    return ''.join(message)


def _zigzag(rails, count):
    if rails < 0:
        raise ValueError("rails must be greater than 1")
    if rails == 1:
        return [1] * count

    direction = UP
    result = [None] * count
    result[0] = 1

    for i in range(1, count):
        if result[i - 1] == 1 and direction == DOWN:
            direction = UP
        if result[i - 1] == rails and direction == UP:
            direction = DOWN

        result[i] = result[i - 1] + direction

    return result
