class Matrix:
    def __init__(self, matrix_string):
        self._matrix = [
            [int(num_string) for num_string in row.split(" ")]
            for row in matrix_string.split("\n")
        ]

    def row(self, index) -> list[int]:
        return self._matrix[index - 1]

    def column(self, index) -> list[int]:
        return [row[index -1] for row in self._matrix]

