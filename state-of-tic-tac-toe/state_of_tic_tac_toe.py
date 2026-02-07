from collections import Counter
MARKS = ("X", "O")

def gamestate(board: list[str]) -> str:
    """Determine the current state of a tic-tac-toe game.
    
    Args:
        board: A list of 3 strings representing the game board rows.
               Each string contains 3 characters: 'X', 'O', or ' '.
    
    Returns:
        'win' if one player has won, 'draw' if the board is full with no winner,
        or 'ongoing' if the game is still in progress.
    
    Raises:
        ValueError: If the board state is impossible (wrong turn order or
                    game continued after a win).
    """
    matrix = [list(row) for row in board]

    _validate_board(matrix)
    if _row_win(matrix) or _column_win(matrix) or _diagonal_win(matrix):
        return "win"
    if _board_full(matrix):
        return "draw"

    return "ongoing"


def _validate_board(matrix: list[list[str]]) -> None:
    """Validate that the board state is possible.
    
    Args:
        matrix: The game board as a 2D list of characters.
    
    Raises:
        ValueError: If X went twice, O started, or the game continued after a win.
    """
    flattened_matrix = [cell for row in matrix for cell in row]
    counts = Counter(flattened_matrix)

    if counts["X"] > counts["O"] + 1:
        raise ValueError("Wrong turn order: X went twice")
    if counts["O"] > counts["X"]:
        raise ValueError("Wrong turn order: O started")
    if _row_win_count(matrix) > 1 or _column_win_count(matrix) > 1:
        raise ValueError("Impossible board: game should have ended after the game was won")


def _row_win(matrix: list[list[str]]) -> bool:
    """Check that there is exactly one winning row."""
    return _row_win_count(matrix) == 1


def _column_win(matrix: list[list[str]]) -> bool:
    """Check that there is exactly one winning column."""
    return _column_win_count(matrix) == 1


def _diagonal_win(matrix: list[list[str]]) -> bool:
    """Check if either diagonal has all matching marks."""
    diagonals = [
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]

    return any(
        all(matrix[i][j] == mark for i, j in diagonal)
        for diagonal in diagonals
        for mark in MARKS
    )


def _board_full(matrix: list[list[str]]) -> bool:
    """Check if the board has no empty spaces."""
    return all(
        cell in MARKS
        for row in matrix
        for cell in row
    )


def _row_win_count(matrix: list[list[str]]) -> int:
    """Count the number of winning rows."""
    return sum(
        1 for row in matrix
        if len(set(row)) == 1 and row[0] in MARKS
    )


def _column_win_count(matrix: list[list[str]]) -> int:
    """Count the number of winning columns."""
    transposed = zip(*matrix)
    return _row_win_count(transposed)
