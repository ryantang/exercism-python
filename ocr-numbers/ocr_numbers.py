NUMBERS = {
    (" _ ", "| |", "|_|", "   "): "0",
    ("   ", "  |", "  |", "   "): "1",
    (" _ ", " _|", "|_ ", "   "): "2",
    (" _ ", " _|", " _|", "   "): "3",
    ("   ", "|_|", "  |", "   "): "4",
    (" _ ", "|_ ", " _|", "   "): "5",
    (" _ ", "|_ ", "|_|", "   "): "6",
    (" _ ", "  |", "  |", "   "): "7",
    (" _ ", "|_|", "|_|", "   "): "8",
    (" _ ", "|_|", " _|", "   "): "9",
}

def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    if any(len(col) % 3 != 0 for col in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    result = []
    for i in range(len(input_grid)//4):
        start_row = i * 4
        end_row = (i + 1) * 4
        bloc = input_grid[start_row:end_row]

        print(f"bloc is {bloc}")
        sections = []
        for j in range(len(bloc[0])//3):
            ascii_digit = []
            start = j * 3
            end = (j + 1) * 3

            for row in bloc:
                ascii_digit.append(row[start:end])

            sections.append(NUMBERS.get(tuple(ascii_digit), "?"))

        result.append("".join(sections))

    return ",".join(result)

