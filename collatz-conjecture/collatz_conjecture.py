def steps(number: int) -> int:
    """ Calculate the number of steps to reach 1 using the Collatz conjecture.
    
    Args:
        number: A positive integer to calculate steps for
        
    Returns:
        int: The number of steps to reach 1
        
    Raises:
        ValueError: If the input number is less than 1
        
    Example:
        >>> steps(12)
        9  # 12→6→3→10→5→16→8→4→2→1
    """
    if (number < 1):
        raise ValueError("Only positive integers are allowed")

    total_steps = 0
    while (number > 1):
        if _is_even(number):
            number = number / 2
            total_steps += 1
        else:
            number = number * 3 + 1
            total_steps +=1
    
    return total_steps

def _is_even(number: int) -> bool:
    return number % 2 == 0

