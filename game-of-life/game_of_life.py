def tick(matrix: list[list[int]]) -> list[list[int]]:
    """Advance the game of life by one generation.
    
    Args:
        matrix: A 2D list representing the current state of the game board.
                1 represents a live cell, 0 represents a dead cell.
    
    Returns:
        A 2D list representing the next generation of the game board.
    """
    if matrix == []:
        return []

    num_rows, num_cols = len(matrix), len(matrix[0])
    new_matrix = [[0] * num_cols for _ in range(num_rows)]

    for row_index, row in enumerate(matrix):
        for col_index, cell in enumerate(row):
            if (cell == 1 and _live_neighbors((row_index, col_index), matrix) in (2,3)
                or cell == 0 and _live_neighbors((row_index, col_index), matrix) == 3):
                new_matrix[row_index][col_index] = 1

    return new_matrix

def _live_neighbors(coordinates: tuple[int, int], matrix: list[list[int]]) -> int:
    """Count the number of live neighbors for a cell at the given coordinates.
    
    Args:
        coordinates: A tuple (row_index, col_index) of the cell's position.
        matrix: The current game board.
    
    Returns:
        The count of live neighbors (0-8).
    """
    row_index, col_index = coordinates
    num_rows, num_cols = len(matrix), len(matrix[0])

    live_neighbors = 0

    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if (i, j) != (0, 0):
                neighbor_row = row_index + i
                neighbor_col = col_index + j
                if (0 <= neighbor_row < num_rows
                    and 0 <= neighbor_col < num_cols):
                    live_neighbors += matrix[neighbor_row][neighbor_col]

    return live_neighbors
