from collections import Counter
MARKS = ("X", "O")

def gamestate(board: list[str]) -> str:
    matrix = [list(row) for row in board]

    _validate_board(matrix)
    if _row_win(matrix) or _column_win(matrix) or _diagonal_win(matrix):
        return "win"
    if _board_full(matrix):
        return "draw"

    return "ongoing"


def _validate_board(matrix: list[list[str]]):
    flattened_matrix = [cell for row in matrix for cell in row]
    counts = Counter(flattened_matrix)

    if counts["X"] > counts["O"] + 1:
        raise ValueError("Wrong turn order: X went twice")
    if counts["O"] > counts["X"]:
        raise ValueError("Wrong turn order: O started")
    if _row_win_count(matrix) > 1 or _column_win_count(matrix) > 1:
        raise ValueError("Impossible board: game should have ended after the game was won")

def _row_win(matrix: list[list[str]]) -> bool:
    return _row_win_count(matrix) == 1

def _column_win(matrix: list[list[str]]) -> bool:
    return _column_win_count(matrix) == 1

def _row_win_count(matrix: list[list[str]]) -> int:
    return sum(
        1 for row in matrix
        if len(set(row)) == 1 and row[0] in MARKS
    )

def _column_win_count(matrix: list[list[str]]) -> int:
    transposed = zip(*matrix)
    return _row_win_count(transposed)

def _diagonal_win(matrix: list[list[str]]) -> bool:
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
    return all(
        cell in MARKS
        for row in matrix
        for cell in row
    )
