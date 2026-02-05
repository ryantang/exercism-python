def tick(matrix):
    if matrix == []:
        return []

    num_rows, num_col = len(matrix), len(matrix[0])
    new_matrix = [[0] * num_col for _ in range(num_rows)]

    for row_index, row in enumerate(matrix):
        for col_index, cell in enumerate(row):
            if (cell == 1 and _live_neighbors((row_index, col_index), matrix) in (2,3)
                or cell == 0 and _live_neighbors((row_index, col_index), matrix) == 3):
                new_matrix[row_index][col_index] = 1

    return new_matrix

def _live_neighbors(coordinates, matrix):
    row_index, col_index = coordinates
    num_rows, num_col = len(matrix), len(matrix[0])

    neighbors = []

    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if (i, j) != (0, 0):
                neighbor_row = row_index + i
                neighbor_col = col_index + j
                if (0 <= neighbor_row < num_rows
                    and 0 <= neighbor_col < num_col):
                    neighbors.append((neighbor_row, neighbor_col))

    return sum(matrix[i][j] for i, j in neighbors)
