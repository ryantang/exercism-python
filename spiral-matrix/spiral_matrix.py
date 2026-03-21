from collections import namedtuple

RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
UP = (-1, 0)

DIRECTIONS = (RIGHT, DOWN, LEFT, UP)
Cell = namedtuple('Cell', ('row_index', 'col_index'))

def spiral_matrix(size):
    matrix = [
        [None] * size
        for _ in range(size)
    ]

    current_cell = Cell(0, -1)
    step = 1
    direction = RIGHT

    print(f'matrix is {matrix}')

    while _next_cell_empty(matrix, current_cell, direction):
        current_cell, step = _fill_to_end(matrix, current_cell, step, direction)
        direction = _turn_right(direction)

    return matrix

def _turn_right(direction):
    index = DIRECTIONS.index(direction)
    new_index = (index + 1) % len(DIRECTIONS)
    return DIRECTIONS[new_index]


def _fill_to_end(matrix, current_cell, step, direction):
    if not _next_cell_empty(matrix, current_cell, direction):
        return (current_cell, step)

    next_cell = Cell(
        row_index = current_cell.row_index + direction[0],
        col_index = current_cell.col_index + direction[1]
    )

    matrix[next_cell.row_index][next_cell.col_index] = step
    step += 1
    current_cell = next_cell

    print(f'current_cell is {current_cell}')
    print(f'matrix is {matrix}\n')

    return _fill_to_end(matrix, current_cell, step, direction)



def _next_cell_empty(matrix: list[list[int|None]], current_cell: tuple[int, int], direction: str) -> bool:
    size = len(matrix)

    next_cell = Cell(
        row_index = current_cell.row_index + direction[0],
        col_index = current_cell.col_index + direction[1]
    )

    return (next_cell.row_index < size and next_cell.col_index < size and
        matrix[next_cell.row_index][next_cell.col_index] is None)
