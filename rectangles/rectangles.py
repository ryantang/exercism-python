from itertools import combinations
from collections import namedtuple
from collections.abc import Iterator

Rectangle = namedtuple('Rectangle', ('top_left', 'top_right', 'bottom_left', 'bottom_right'))
Point = namedtuple('Point', ('row_index', 'col_index'))


def rectangles(strings: list[str]) -> int:
    """Count the number of rectangles in an ASCII diagram."""
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

    return sum(
        1 for candidate in _candidate_rectangles(plus_combos)
        if _valid_rectangle(matrix, candidate)
    )

def _candidate_rectangles(plus_combos: list[list[tuple[int, int]]]) -> Iterator[Rectangle]:
    """Yield rectangles formed by matching column pairs across row pairs."""
    for top_index in range(len(plus_combos)): # pylint: disable=consider-using-enumerate
        for bottom_index in range(top_index + 1, len(plus_combos)):
            matching_combos = set(plus_combos[top_index]) & set(plus_combos[bottom_index])
            for combo in matching_combos:
                left_index, right_index = combo
                yield Rectangle(
                    top_left = Point(top_index, left_index),
                    top_right = Point(top_index, right_index),
                    bottom_left = Point(bottom_index, left_index),
                    bottom_right = Point(bottom_index, right_index)
                )


def _valid_rectangle(matrix: list[list[str]], candidate: Rectangle) -> bool:
    """Check if all edges of a candidate rectangle are properly filled."""
    top_edge = _edge(candidate.top_left, candidate.top_right)
    bottom_edge = _edge(candidate.bottom_left, candidate.bottom_right)
    left_edge = _edge(candidate.top_left, candidate.bottom_left)
    right_edge = _edge(candidate.top_right, candidate.bottom_right)

    horizontal_edges_filled = _filled(matrix, top_edge + bottom_edge, "+-")
    vertical_edges_filled = _filled(matrix, left_edge + right_edge, "+|")

    return horizontal_edges_filled and vertical_edges_filled

def _filled(matrix: list[list[str]], edges: list[Point], valid_symbols: str) -> bool:
    """Return whether all edge cells contain valid symbols."""
    return all(matrix[i][j] in valid_symbols for i, j in edges)

def _edge(corner1: Point, corner2: Point) -> list[Point]:
    """Return the coordinates of all cells between two corners."""
    if corner1.row_index == corner2.row_index: # horizontal edge
        return [
            Point(corner1.row_index, col_index)
            for col_index in range(corner1.col_index, corner2.col_index + 1)
        ]
    if corner1.col_index == corner2.col_index: # vertical edge
        return [
            Point(row_index, corner1.col_index)
            for row_index in range(corner1.row_index, corner2.row_index + 1)
        ]

    raise ValueError("corners are not vertices of a rectangle")
