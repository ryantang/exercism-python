from collections import namedtuple

Point = namedtuple('Point', ('row_index', 'col_index'))

class ConnectGame:
    def __init__(self, board):
        rows = board.split('\n')
        self.matrix = [
            list(row.split())
            for row in rows
        ]

        self.board_height = len(self.matrix)
        self.board_width = len(self.matrix[0])

        print(f'matrix is {self.matrix}')

    def get_winner(self):
        if self._empty_board():
            return ''

        x_left_edge = []
        for row_index, row in enumerate(self.matrix):
            if row[0] == 'X':
                x_left_edge.append(Point(row_index=row_index, col_index=0))

        for start_node in x_left_edge:
            if self._complete_path('X', [start_node]):
                return 'X'

        o_top_edge = []
        for col_index, node in enumerate(self.matrix[0]):
            if node == 'O':
                o_top_edge.append(Point(row_index=0, col_index=col_index))

        for start_node in o_top_edge:
            if self._complete_path('O', [start_node]):
                return 'O'

        return ''


    def _complete_path(self, player, path):
        if not path:
            raise ValueError('Function _complete_path requires a starting node')

        # Win conditions
        current_node = path[-1]
        if player == 'X' and current_node.col_index == self.board_width - 1:
            return True
        if player == 'O' and current_node.row_index == self.board_height - 1:
            return True

        possible_next_nodes = self._neighbors(path[-1], player) - set(path)
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
            row_index = node.row_index + delta.row_index
            col_index = node.col_index + delta.col_index

            candidate = Point(row_index, col_index)

            if self._on_board(candidate):
                if self.matrix[row_index][col_index] == player:
                    neighbors.add(candidate)

        return neighbors

    def _on_board(self, node):
        return  (0 <= node.row_index < self.board_height
                    and 0 <= node.col_index < self.board_width)


    def _empty_board(self):
        return all(
            cell == '.'
            for row in self.matrix
            for cell in row
        )
