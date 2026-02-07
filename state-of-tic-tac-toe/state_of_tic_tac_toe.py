def gamestate(board):
    matrix = []
    for row in board:
        matrix.append(list(row))

    if _row_win_count(matrix) > 1 or _column_win_count(matrix) > 1:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if _player_x_went_twice(matrix):
        raise ValueError("Wrong turn order: X went twice")
    if _player_o_went_first(matrix):
        raise ValueError("Wrong turn order: O started")

    if _row_win_count(matrix) + _column_win_count(matrix) + _diagonal_win_count(matrix) >= 1:
        return "win"

    if _board_full(matrix):
        return "draw"

    return "ongoing"


def _player_x_went_twice(matrix):
    total_x = 0
    total_o = 0

    for row in matrix:
        for cell in row:
            if cell == "X":
                total_x += 1
            if cell == "O":
                total_o += 1

    return total_x > total_o + 1


def _player_o_went_first(matrix):
    total_x = 0
    total_o = 0

    for row in matrix:
        for cell in row:
            if cell == "X":
                total_x += 1
            if cell == "O":
                total_o += 1

    return total_o > total_x

def _row_win_count(matrix):
    row_win_count = 0

    for row in matrix:
        if all(cell == "X" for cell in row) or all(cell == "O" for cell in row):
            row_win_count += 1

    return row_win_count

def _column_win_count(matrix):
    transposed = [[None]* 3 for _ in range(3)]
    for row_index, row in enumerate(matrix):
        for col_index, cell in enumerate(row):
            transposed[col_index][row_index] = cell

    return _row_win_count(transposed)

def _diagonal_win_count(matrix):
    diag1 = [(0,0), (1,1), (2,2)]
    diag2 = [(0,2), (1,1), (2,0)]
    diagonal_win_count = 0

    if all(matrix[i][j] == "X" for i, j in diag1):
        diagonal_win_count += 1
    if all(matrix[i][j] == "X" for i, j in diag2):
        diagonal_win_count += 1
    if all(matrix[i][j] == "O" for i, j in diag1):
        diagonal_win_count += 1
    if all(matrix[i][j] == "O" for i, j in diag2):
        diagonal_win_count += 1

    return diagonal_win_count

def _board_full(matrix):
    return all(
        cell in ("X","O")
        for row in matrix
        for cell in row
    )
