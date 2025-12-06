class Queen:
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
        
        # check diagonals
        return abs(self.row - another_queen.row) == abs(self.column - another_queen.column)
    
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