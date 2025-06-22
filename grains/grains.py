def square(number: int) -> int:
    """ Calculate the grains of rice on a square of the chessboard
    
    Args:
        number: The square number on the chessboard (1-64)
        
    Returns:
        int: Number of grains on that square (doubles each time)
        
    Raises:
        ValueError: If square number is not between 1 and 64
    """
    if not (1 <= number <= 64):
        raise ValueError('square must be between 1 and 64')

    return 2 ** (number - 1)

def total() -> int:
    """Calculate the total number of grains on all squares.
    
    Returns:
        int: Sum of grains on all 64 squares of the chessboard
    """

    return sum(square(number) for number in range(1,65))
    