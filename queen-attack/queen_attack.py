class Queen:
    BOARD_MIN = 0
    BOARD_MAX = 7

    def __init__(self, row, column):
        self._validate(row, column)
        self._row = row
        self._column = column

    @property
    def row(self):
        return self._row

    @property
    def column(self):
        return self._column
    
    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        if self.row == another_queen.row:
            return True
        
        if self.column == another_queen.column:
            return True
        
        directions = {
            "up_right": (1, 1),
            "up_left": (1, -1),
            "down_right": (-1, 1),
            "down_left": (-1, -1),
        }

        return self._check_diagonals(another_queen, directions)
    
    def _check_diagonals(self, other_queen, directions):
        for direction in directions.values():
            row = self.row
            column = self.column
            while self._in_boundary(row, column):
                row += direction[0]
                column += direction[1]
                if other_queen.row == row and other_queen.column == column:
                    return True
        return False

    @staticmethod
    def _in_boundary(row, column):
        return Queen.BOARD_MIN <= row <= Queen.BOARD_MAX and Queen.BOARD_MIN <= column <= Queen.BOARD_MAX

    @staticmethod
    def _validate(row, column):
        validations = {
            "row": row,
            "column": column,
        }

        for row_or_col, value in validations.items():
            if value < 0:
                raise ValueError(f"{row_or_col} not positive")
            if value > Queen.BOARD_MAX:
                raise ValueError(f"{row_or_col} not on board")