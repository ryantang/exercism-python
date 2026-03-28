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

    current_cell = Cell(0, 0)
    step = 1
    direction = RIGHT

    while _within_matrix(matrix, current_cell) and _cell_empty(matrix, current_cell):
        current_cell, step = _fill_to_end(matrix, current_cell, step, direction)
        direction = _turn_right(direction)
        current_cell = _next_cell(current_cell, direction)

    return matrix

def _turn_right(direction):
    index = DIRECTIONS.index(direction)
    new_index = (index + 1) % len(DIRECTIONS)
    return DIRECTIONS[new_index]


def _fill_to_end(matrix, current_cell, step, direction):
    if not _cell_empty(matrix, current_cell):
        return (current_cell, step)

    matrix[current_cell.row_index][current_cell.col_index] = step
    step += 1

    next_cell = _next_cell(current_cell, direction)

    if not _within_matrix(matrix, next_cell) or not _cell_empty(matrix, next_cell):
        return (current_cell, step)

    current_cell = next_cell
    print(f'current_cell is {current_cell}')
    print(f'matrix is {matrix}\n')

    return _fill_to_end(matrix, current_cell, step, direction)


def _cell_empty(matrix: list[list[int|None]], cell: tuple[int, int]) -> bool:
    return matrix[cell.row_index][cell.col_index] is None

def _within_matrix(matrix, cell) -> bool:
    size = len(matrix)
    return cell.row_index < size and cell.col_index < size

def _next_cell(current_cell, direction):
    potential_next_cell = Cell(
        row_index = current_cell.row_index + direction[0],
        col_index = current_cell.col_index + direction[1]
    )

    return potential_next_cell
