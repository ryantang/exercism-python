import math

def egg_count(display_value):
    eggs = 0
    remaining = display_value

    while remaining > 0:
        eggs += remaining % 2
        remaining = remaining//2

    return eggs