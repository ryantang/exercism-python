from collections import namedtuple

Cell = namedtuple('Cell', ['row_ind', 'col_ind'] )
Delta = namedtuple('Delta', ['row_ind', 'col_ind'] )

NEIGHBOR_DELTAS = (
    Delta(-1, -1), Delta(-1, 0), Delta(-1, 1),
    Delta(0, -1), Delta(0, 1),
    Delta(1, -1), Delta(1, 0), Delta(1, 1)
)

VALID_CHARACTERS = {'*', ' '}

def annotate(garden: list[str]) -> list[str]:
    """
    Annotates a garden with the number of adjacent flowers.

    Args:
        garden: A list of strings representing the garden, where '*' is a flower.

    Returns:
        A list of strings with spaces replaced by the count of adjacent flowers.

    Raises:
        ValueError: If the garden is invalid (e.g., unequal row lengths or
                    contains invalid characters).
    """
    if not garden:
        return []

    num_rows = len(garden)
    num_cols = len(garden[0])

    if _unequal_columns(garden) or _has_invalid_character(garden):
        raise ValueError("The board is invalid with current input.")

    matrix = [list(row) for row in garden]

    for row_ind, row in enumerate(garden):
        for col_ind, cell in enumerate(row):
            if cell != "*":
                matrix[row_ind][col_ind] = _fill(num_rows, num_cols, matrix, row_ind, col_ind)

    return [''.join(row) for row in matrix]

def _unequal_columns(garden):
    """Checks if all rows in the garden have the same number of columns."""
    return any(len(row) != len(garden[0]) for row in garden)

def _has_invalid_character(garden: list[str]) -> bool:
    """Checks if the garden contains any characters other than '*' or ' '."""
    return any(
        char not in VALID_CHARACTERS
        for row in garden
        for char in row
        )


def _fill(num_rows: int, num_cols: int, matrix: list[list[str]], row_ind: int, col_ind: int) -> str:
    """
    Calculates the number of adjacent flowers for a given cell.

    Args:
        num_rows: The total number of rows in the garden.
        num_cols: The total number of columns in the garden.
        matrix: The garden represented as a list of lists of characters.
        row_ind: The row index of the cell to check.
        col_ind: The column index of the cell to check.

    Returns:
        A string representing the number of adjacent flowers, or a space if there are none.
    """
    flowering_neighbors = 0

    for delta in NEIGHBOR_DELTAS:
        neighbor = Cell(row_ind=row_ind+delta.row_ind, col_ind=col_ind+delta.col_ind)
        if (num_rows > neighbor.row_ind >= 0 and num_cols > neighbor.col_ind >=0 and
            matrix[neighbor.row_ind][neighbor.col_ind] == '*'):
            flowering_neighbors += 1

    return str(flowering_neighbors) if flowering_neighbors > 0 else ' '
