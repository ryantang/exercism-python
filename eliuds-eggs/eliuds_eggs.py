def egg_count(display_value):
    digits = 0
    while (2 ** digits) < display_value:
        digits += 1

    eggs = 0
    remainder = display_value
    while remainder > 0:
        if 2 ** digits <= remainder:
            eggs += 1
            remainder -= 2 ** digits

        digits -= 1

    return eggs
