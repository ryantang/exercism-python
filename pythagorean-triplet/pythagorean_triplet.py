"""
Find Pythagorean triplets that sum to a given number.

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
a² + b² = c².
"""

# Minimum value for any leg in a Pythagorean triplet (from the triplet 3, 4, 5)
SMALLEST_PYTHAGOREAN_TRIPLET_LEG = 3


def triplets_with_sum(number):
    """
    Find all Pythagorean triplets whose sum equals the given number.
    
    Uses an optimized search with tight bounds:
    - Outer loop iterates over possible hypotenuse values (c)
    - Inner loop iterates over possible smallest leg values (a)
    - Computes b directly from the sum constraint
    
    Args:
        number: The target sum for the triplet (a + b + c)
    
    Returns:
        A list of lists, where each inner list represents a triplet [a, b, c]
        satisfying a < b < c and a² + b² = c² and a + b + c = number
    
    Example:
        >>> triplets_with_sum(12)
        [[3, 4, 5]]
        >>> triplets_with_sum(30)
        [[5, 12, 13]]
    """
    triplets = []

    # c must be at least number/3 (when a, b, c are roughly equal)
    # and at most number/2 (since a + b > c for valid triangles)
    c_min = number // 3
    c_max = number // 2
    
    for c in range(c_min, c_max + 1):
        # Triangle inequality: a + b > c
        # Since a + b = number - c, we need number - c > c
        if number - c <= c:
            break

        # Precompute c² to avoid recalculating in the inner loop
        c_squared = c ** 2
        
        # a must satisfy:
        # 1. a >= 3 (minimum triplet leg size)
        # 2. a + b > c (triangle inequality) → a > 2c - number
        a_min = max(SMALLEST_PYTHAGOREAN_TRIPLET_LEG, 2 * c - number + 1)
        
        # a must also satisfy:
        # 1. a < c (ordering constraint)
        # 2. a < b, and since a + b = number - c, this means a < (number - c) / 2
        a_max = min(c - 1, (number - c) // 2)
        
        for a in range(a_min, a_max + 1):
            b = number - a - c
            if a ** 2 + b ** 2 == c_squared:
                triplets.append([a, b, c])
    
    return triplets
