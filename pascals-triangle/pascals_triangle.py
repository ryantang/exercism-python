def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    if row_count == 0:
        return []

    return triangle([[1]], row_count)



def triangle(accmulated_rows, max_count):
    if len(accmulated_rows) == max_count:
        return accmulated_rows

    previous_row = accmulated_rows[-1]
    middle_numbers = [
        num + previous_row[index + 1]
        for index, num in enumerate(previous_row[:-1])
    ]
    row = [1] + middle_numbers + [1]

    return triangle(accmulated_rows + [row], max_count)
