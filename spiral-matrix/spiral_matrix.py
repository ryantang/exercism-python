from collections import namedtuple

Cell = namedtuple('Cell', ['row_index', 'col_index'])
Delta = namedtuple('Delta', ['row_delta', 'col_delta'])

RIGHT = Delta(0, 1)
DOWN = Delta(1, 0)
LEFT = Delta(0, -1)
UP = Delta(-1, 0)
DIRECTIONS = (RIGHT, DOWN, LEFT, UP)

def spiral_matrix(size: int) -> list[list[int]]:
    matrix = [
        [None] * size
        for _ in range(size)
    ]

    cell = Cell(0, 0)
    direction = RIGHT

    for i in range(size ** 2):
        matrix[cell.row_index][cell.col_index] = i + 1
        forward_cell = _forward_cell(cell, direction)

        if (_in_boundary(size, forward_cell) and
            matrix[forward_cell.row_index][forward_cell.col_index] is None):
            cell = forward_cell
        else:
            direction = _turn_right(direction)
            cell = _forward_cell(cell, direction)

    return matrix

def _in_boundary(matrix_size: int, cell):
    return cell.row_index < matrix_size and cell.col_index < matrix_size

def _turn_right(direction):
    index = (DIRECTIONS.index(direction) + 1) % len(DIRECTIONS)
    return DIRECTIONS[index]

def _forward_cell(cell, direction):
    return Cell(
            cell.row_index + direction.row_delta,
            cell.col_index + direction.col_delta
    )
