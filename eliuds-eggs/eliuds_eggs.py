import math

def egg_count(display_value):
    if display_value == 0:
        return 0

    digits = math.ceil(math.log2(display_value))

    eggs = 0
    remainder = display_value
    while remainder > 0:
        if 2 ** digits <= remainder:
            eggs += 1
            remainder -= 2 ** digits

        digits -= 1

    return eggs
