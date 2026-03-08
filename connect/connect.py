from collections import namedtuple

Point = namedtuple('Point', ('row_index', 'col_index'))

class ConnectGame:
    PLAYER_X = 'X'
    PLAYER_O = 'O'

    def __init__(self, board):
        rows = board.split('\n')
        self.matrix = [
            list(row.split())
            for row in rows
        ]

        self.board_height = len(self.matrix)
        self.board_width = len(self.matrix[0])

    def get_winner(self):
        x_left_edge = (
            Point(row_index=row_index, col_index=0)
            for row_index, row in enumerate(self.matrix)
            if row[0] == self.PLAYER_X
        )

        for start_node in x_left_edge:
            if self._complete_path(self.PLAYER_X, [start_node]):
                return self.PLAYER_X

        o_top_edge = (
            Point(row_index=0, col_index=col_index)
            for col_index, node in enumerate(self.matrix[0])
            if node == self.PLAYER_O
        )

        for start_node in o_top_edge:
            if self._complete_path(self.PLAYER_O, [start_node]):
                return self.PLAYER_O

        return ''


    def _complete_path(self, player, path):
        # Win conditions
        current_node = path[-1]
        if player == self.PLAYER_X and current_node.col_index == self.board_width - 1:
            return True
        if player == self.PLAYER_O and current_node.row_index == self.board_height - 1:
            return True

        possible_next_nodes = self._neighbors(current_node, player) - set(path)
        for node in possible_next_nodes:
            if self._complete_path(player, path + [node]):
                return True

        return False

    def _neighbors(self, node, player):
        deltas = (
            Point(0, 1),
            Point(0, -1),
            Point(1, 0),
            Point(-1, 0),
            Point(-1, 1),
            Point(1, -1)
        )

        neighbors = set()
        for delta in deltas:
            candidate = Point(
                row_index = node.row_index + delta.row_index,
                col_index = node.col_index + delta.col_index
            )
            if (self._on_board(candidate)
                    and self.matrix[candidate.row_index][candidate.col_index] == player):
                neighbors.add(candidate)

        return neighbors

    def _on_board(self, node):
        return  (0 <= node.row_index < self.board_height
                    and 0 <= node.col_index < self.board_width)
