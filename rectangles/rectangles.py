def rectangles(strings):
    if not strings:
        return 0




    rows_of_plusses = []
    for row in strings:
        plus_cols = []
        for col_ind, char in enumerate(row):
            if char == '+':
                plus_cols.append(col_ind)
        rows_of_plusses.append(plus_cols)

    plus_combos = []
    for row in rows_of_plusses:
        plus_combos.append(_combinations(row))


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

    print(f'candidates is {candidates}')

    valid_rectangles = (
        1
        for candidate in candidates
        if _check_rectangle(strings, candidate)
    )

    # return "break test intentionally"
    return sum(valid_rectangles)

    # return len(candidates)


def _check_rectangle(strings, candidate) -> bool:

    col_width = max(len(string) for string in strings)

    matrix = [
        list(string.ljust(col_width))
        for string in strings
    ]

    edge_coordinates = {
        *_edge(candidate[0], candidate[1]),
        *_edge(candidate[2], candidate[3]),
        *_edge(candidate[0], candidate[2]),
        *_edge(candidate[1], candidate[3])
    }

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


def _combinations(items):
    combinations = []
    for i, item in enumerate(items):
        remainder = items[i+1:]
        combinations += list(zip([item] * len(remainder), remainder ))

    return combinations



    #change into matrix
    #get '+' coordinates
    #for each row, get all combination of two '+' coordinates
    #   for each row below original row, see if there's another matching set of two '+'s
    #       if so, increment number of rectangles    
