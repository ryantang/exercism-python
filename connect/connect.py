from collections import namedtuple

Point = namedtuple('Point', ('row_index', 'col_index'))

class ConnectGame:
    """Represents a Hex/Polygon board and determines the winner."""

    PLAYER_X = 'X'
    PLAYER_O = 'O'
    DELTAS = (
        Point(0, 1),
        Point(0, -1),
        Point(1, 0),
        Point(-1, 0),
        Point(-1, 1),
        Point(1, -1)
    )

    def __init__(self, board: str) -> None:
        """Parse the board string into a 2D matrix of cell values."""
        rows = board.split('\n')
        self.matrix = [
            list(row.split())
            for row in rows
        ]

        self.board_height = len(self.matrix)
        self.board_width = len(self.matrix[0])

    def get_winner(self) -> str:
        """Return 'X' if X has won, 'O' if O has won, or '' if there is no winner."""
        x_left_edge = (
            Point(row_index=row_index, col_index=0)
            for row_index, row in enumerate(self.matrix)
            if row[0] == self.PLAYER_X
        )

        for start_node in x_left_edge:
            if self._complete_path(self.PLAYER_X, start_node):
                return self.PLAYER_X

        o_top_edge = (
            Point(row_index=0, col_index=col_index)
            for col_index, node in enumerate(self.matrix[0])
            if node == self.PLAYER_O
        )

        for start_node in o_top_edge:
            if self._complete_path(self.PLAYER_O, start_node):
                return self.PLAYER_O

        return ''


    def _complete_path(self, player: str, start_node: Point) -> bool:
        """Return True if a path exists from start_node to the player's winning edge."""
        visited = set()
        stack = [start_node]

        while stack:
            node = stack.pop()

            # Avoid loops
            if node in visited:
                continue

            if self._win_conditions(player, node):
                return True

            visited.add(node)
            for neighbor in self._neighbors(node, player):
                if neighbor not in visited:
                    stack.append(neighbor)

        return False


    def _win_conditions(self, player: str, node: Point) -> bool:
        """Return True if the given node satisfies the win condition for the given player."""
        x_win = (player == self.PLAYER_X and node.col_index == self.board_width - 1)
        o_win = (player == self.PLAYER_O and node.row_index == self.board_height - 1)

        return x_win or o_win


    def _neighbors(self, node: Point, player: str) -> set[Point]:
        """Return the set of adjacent nodes occupied by the given player."""
        neighbors = set()
        for delta in self.DELTAS:
            candidate = Point(
                row_index = node.row_index + delta.row_index,
                col_index = node.col_index + delta.col_index
            )
            if (self._on_board(candidate)
                    and self.matrix[candidate.row_index][candidate.col_index] == player):
                neighbors.add(candidate)

        return neighbors


    def _on_board(self, node: Point) -> bool:
        """Return True if the given node is within the board boundaries."""
        return (0 <= node.row_index < self.board_height
                and 0 <= node.col_index < self.board_width)
