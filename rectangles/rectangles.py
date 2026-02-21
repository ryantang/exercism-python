from itertools import combinations

def rectangles(strings):
    if not strings:
        return 0

    col_width = max(len(string) for string in strings)

    matrix = [
        list(string.ljust(col_width))
        for string in strings
    ]

    rows_of_plusses = [
        [col_index for col_index, cell in enumerate(row) if cell == '+']
        for row in matrix
    ]

    plus_combos = [
        list(combinations(row, 2))
        for row in rows_of_plusses
    ]

    candidates = []
    for top_index, top_row in enumerate(plus_combos):
        for bottom_index, bottom_row in enumerate(plus_combos[top_index + 1:]):
            for combo in top_row:
                if combo in bottom_row:
                    candidate = (
                        (top_index, combo[0]),
                        (top_index, combo[1]),
                        (bottom_index + top_index + 1, combo[0]),
                        (bottom_index + top_index + 1, combo[1])
                    )
                    candidates.append(candidate)

    valid_rectangles = (
        1
        for candidate in candidates
        if _check_rectangle(matrix, candidate)
    )

    # return "break intentionally"
    return sum(valid_rectangles)

def _check_rectangle(matrix, candidate) -> bool:

    top_edge = _edge(candidate[0], candidate[1])
    bottom_edge = _edge(candidate[2], candidate[3])
    left_edge = _edge(candidate[0], candidate[2])
    right_edge = _edge(candidate[1], candidate[3])

    top_edge_filled = _horizontal_filled(matrix, top_edge)
    bottom_edge_filled = _horizontal_filled(matrix, bottom_edge)
    left_edge_filled = _vertical_filled(matrix, left_edge)
    right_edge_filled = _vertical_filled(matrix, right_edge)

    return all(top_edge_filled) and all(bottom_edge_filled) and all(left_edge_filled) and all(right_edge_filled)

def _horizontal_filled(matrix, edges):
    return [
        matrix[i][j] in "+-"
        for i, j in edges
    ]

def _vertical_filled(matrix, edges):
    return [
        matrix[i][j] in "+|"
        for i, j in edges
    ]


def _edge(corner1, corner2):
    edge_coordinates = []

    if corner1[0] == corner2[0]:
        for i in range(corner1[1],corner2[1]+1):
            edge_coordinates.append((corner1[0], i))
    elif corner1[1] == corner2[1]:
        for i in range(corner1[0],corner2[0]+1):
            edge_coordinates.append((i, corner1[1]))
    else:
        raise ValueError("not verticess of a rectangle")

    return edge_coordinates
