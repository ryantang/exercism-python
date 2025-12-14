import math

def egg_count(display_value):
    eggs = 0
    number = display_value

    while number > 0:
        eggs += number % 2
        number = number//2

    return eggs
