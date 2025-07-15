from string import ascii_uppercase

def rows(letter):
    midpoint_index = ascii_uppercase.index(letter)

    my_rows = []
    for i, letter in enumerate(ascii_uppercase[:midpoint_index + 1]):
        buffer_size = midpoint_index - i
        buffer = ' ' * buffer_size

        if i == 0:
            my_rows += [f'{buffer}{letter}{buffer}']
        else:
            middle_size = 1 + (i - 1) * 2
            middle = ' ' * middle_size

            my_rows += [f'{buffer}{letter}{middle}{letter}{buffer}']

    return my_rows + my_rows[-2::-1]
