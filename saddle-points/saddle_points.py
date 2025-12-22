def saddle_points(matrix):
    if not _regular(matrix):
        raise ValueError("irregular matrix")

    if not matrix:
        return []

    candidates_x = _highest_in_row(matrix)
    candidates_y = _lowest_in_col(matrix)
    return _convert(candidates_x & candidates_y)


def _lowest_in_col(matrix):
    result = set()
    low_vals = matrix[0].copy()
    for row in matrix:
        for i, val in enumerate(row):
            if val < low_vals[i]:
                low_vals[i] = val

    for row_index, row in enumerate(matrix):
        for col_index, val in enumerate(row):
            if val == low_vals[col_index]:
                result.add((row_index, col_index))

    return result


def _highest_in_row(matrix):
    result = set()
    for row_index, row in enumerate(matrix):
        row_max = max(row)
        for col_index, val in enumerate(row):
            if val == row_max:
                result.add((row_index, col_index))
    return result


def _convert(results):
    converted = []
    for row_index, col_index in results:
        converted.append({"row": row_index + 1, "column": col_index + 1})
    return converted


def _regular(matrix) -> bool:
    for row in matrix:
        if len(row) != len(matrix[0]):
            return False
    return True
