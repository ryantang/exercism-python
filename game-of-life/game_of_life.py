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
            else:
                next_matrix[row_index][column_index] = 0

    return next_matrix

def _live_neighbors(coordinates, matrix):
    row_index, column_index = coordinates
    neighbors = []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in (-1, 1):
        y = row_index + i
        if 0 <= y <= num_rows - 1:
            for j in (-1, 0, 1):
                x = column_index + j
                if 0 <= x <= num_cols - 1:
                    neighbors.append((y,x))
    for j in (-1, 1):
        y = row_index
        x = column_index + j
        if 0 <= x <= num_cols - 1:
            neighbors.append((y,x))

    print(f'y ix {y} and x is {x}')
    return sum(matrix[y][x] for y, x in neighbors)
