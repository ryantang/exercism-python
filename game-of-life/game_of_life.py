def tick(matrix):
    if matrix == []:
        return matrix

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    next_matrix = [[0] * num_cols for _ in range(num_rows)]

    for row_index, row in enumerate(matrix):
        for column_index, cell in enumerate(row):
            if cell == 1 and _live_neighbors((row_index,column_index), matrix) in (2, 3):
                next_matrix[row_index][column_index] = 1
            elif cell == 0 and _live_neighbors((row_index,column_index), matrix) == 3:
                next_matrix[row_index][column_index] = 1

    return next_matrix

def _live_neighbors(coordinates, matrix):
    row_index, column_index = coordinates
    neighbors = []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in (-1, 0, 1):
        y = row_index + i
        if 0 <= y < num_rows :
            for j in (-1, 0, 1):
                x = column_index + j
                if 0 <= x < num_cols and (i, j) != (0,0):
                    neighbors.append((y, x))

    return sum(matrix[y][x] for y, x in neighbors)
