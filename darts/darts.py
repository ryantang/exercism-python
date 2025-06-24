def score(x: float, y: float) -> int:
    """Calculate the score for a dart landing at (x,y).
    
    Args:
        x: x-coordinate of where the dart lands
        y: y-coordinate of where the dart lands
        
    Returns:
        int: Points scored based on distance from center
    """
    if _in_circle(x, y, radius['inner']):
        return points['inner']
    if _in_circle(x, y, radius['middle']):
        return points['middle']
    if _in_circle(x, y, radius['outer']):
        return points['outer']
    
    return points['miss']
    
points = {
    'inner': 10,
    'middle': 5,
    'outer': 1,
    'miss': 0
}

radius = {
    'inner': 1,
    'middle': 5,
    'outer': 10,
}

def _in_circle(x, y, radius) -> bool:
    return (x ** 2) + (y ** 2)  <= radius ** 2