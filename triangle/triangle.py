def equilateral(sides) -> bool:
    """Determine whether a triangle is equilateral

    Args:
        sides: List of three numbers representing the triange side lengths
    
    Returns:
        bool: True if the triange is equialteral, False if not

    Example:
    >>> equilateral([2, 2, 2])
    True
    >>> equilateral([2, 3, 2])
    False
    """
    return _valid_triangle(sides) and (sides[0] == sides[1] == sides[2])


def isosceles(sides) -> bool:
    """Determine whether a triangle is isoceles

    Args:
        sides: List of three numbers representing the triange side lengths
    
    Returns:
        bool: True if the triange is isoceles, False if not

    Example:
    >>> isoceles([2, 3, 2])
    True
    >>> isoceles([2, 3, 4])
    False
    >>> isoceles([2, 2, 2]) #counting equilateral trianges as isosceles
    True
    """
    return _valid_triangle(sides) and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])


def scalene(sides):
    """Determine whether a triangle is scalene

    Args:
        sides: List of three numbers representing the triange side lengths
    
    Returns:
        bool: True if the triange is isoceles, False if not

    Example:
    >>> isoceles([2, 3, 2])
    True
    >>> isoceles([2, 3, 4])
    False
    """
    return _valid_triangle(sides) and not isosceles(sides)


def _valid_triangle(sides) -> bool:
    """Determine whether the lengths of the sides can make a valid triangle

    Args:
        sides: List of three numbers representing the triange side lengths
    
    Returns:
        bool: True if the sides can make a valid triangle, False if not
    """
    return _all_sides_larger_than_zero(sides) and _side_lengths_valid(sides)


def _all_sides_larger_than_zero(sides) -> bool:
    """Ensure the side lengths are valid

    Args:
        sides: List of three numbers representing the triange side lengths
    
    Returns:
        bool: True if every side length is greater than zero, False if not
    """
    return min(sides) > 0


def _side_lengths_valid(sides):
    """For a triangle to be valid, the longest side must be shorter than 
    the sum of the other two sides

    Args:
        sides: List of three numbers representing the triange side lengths
    
    Returns:
        bool: True if the side lengths are valid, False if not
    """

    max_length = max(sides)
    remaining_sides = sum(sides) - max_length

    return max_length < remaining_sides