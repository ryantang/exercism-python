class Matrix:
    def __init__(self, matrix_string):

        self._matrix = []

        rows = matrix_string.split("\n")
        for i, row in enumerate(rows):
            self._matrix.append(
                [int(num_string) for num_string in row.split(" ")]
            )

    def row(self, index):
        return self._matrix[index - 1]

    def column(self, index):
        return [row[index -1] for row in self._matrix]

