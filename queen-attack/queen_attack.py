class Queen:
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

        row = self.row
        column = self.column
        while row < 7 and column < 7:
            row += 1
            column += 1
            if another_queen.row == row and another_queen.column == column:
                return True
            
        row = self.row
        column = self.column
        while row < 7 and column > 0:
            row += 1
            column -= 1
            if another_queen.row == row and another_queen.column == column:
                return True
            
        row = self.row
        column = self.column
        while row > 0 and column < 7:
            row -= 1
            column += 1
            if another_queen.row == row and another_queen.column == column:
                return True
            
        row = self.row
        column = self.column
        while row > 0 and column > 0:
            row -= 1
            column -= 1
            if another_queen.row == row and another_queen.column == column:
                return True


        return False

    @staticmethod
    def _validate(row, column):
        validations = {
            "row": row,
            "column": column,
        }

        for row_or_col, value in validations.items():
            if value < 0:
                raise ValueError(f"{row_or_col} not positive")
            if value > 7:
                raise ValueError(f"{row_or_col} not on board")