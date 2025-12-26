from collections.abc import Iterator

ASCII_TO_DIGIT = {
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

ASCII_DIGIT_ROWS = 4
ASCII_DIGIT_COLS = 3

def convert(input_grid: list[str]) -> str:
    """Convert ASCII art to digit strings
    
    Args:
        input_grid: List of strings representing ASCII art digits
        
    Returns:
        Comma-separated string of recognized digits
        
    Raises:
        ValueError: If dimensions aren't multiples of 4 and 3
    """
    if len(input_grid) % ASCII_DIGIT_ROWS != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    if any(len(col) % ASCII_DIGIT_COLS != 0 for col in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    result = []
    for bloc in _chunk_row_blocs(input_grid):
        digits = [
            ASCII_TO_DIGIT.get(ascii_digit, "?")
            for ascii_digit in _chunk_single_digit(bloc)
        ]
        result.append("".join(digits))

    return ",".join(result)

def _chunk_row_blocs(grid: list[str]) -> Iterator[list[str]]:
    """Chunks off one grouping of ascii art characters"""
    for i in range(0, len(grid), ASCII_DIGIT_ROWS):
        yield grid[i:i + ASCII_DIGIT_ROWS]


def _chunk_single_digit(bloc: list[str]) -> Iterator[tuple[str, ...]]:
    """Chunks off a single digit in ascii art"""
    for i in range(0, len(bloc[0]), ASCII_DIGIT_COLS):
        yield tuple(row[i:i + ASCII_DIGIT_COLS] for row in bloc)
