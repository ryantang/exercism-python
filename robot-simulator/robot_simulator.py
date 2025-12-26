# Globals for the directions
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot:
    """A robot simulator that tracks position and direction on a grid.
    
    Attributes:
        direction: The direction the robot is facing (NORTH, EAST, SOUTH, or WEST).
        coordinates: The (x, y) position of the robot on the grid.
    """
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._direction = direction

    @property
    def coordinates(self):
        """ returned stored tuple of x and y coordinates"""
        return (self._x_pos, self._y_pos)

    @property
    def direction(self):
        """ returns stored direction """
        return self._direction

    def move(self, instructions):
        """Execute a series of movement instructions.
        
        Args:
            instructions (str): A string of commands where each character is an instruction:
                - 'R': Turn right 90 degrees
                - 'L': Turn left 90 degrees
                - 'A': Advance one unit in the current direction
        """
        for instruction in instructions:
            match instruction:
                case "R":
                    self._direction = (self._direction + 1) % 4
                case "L":
                    self._direction = (self._direction - 1) % 4
                case "A" if self.direction == NORTH:
                    self._y_pos += 1
                case "A" if self.direction == SOUTH:
                    self._y_pos -= 1
                case "A" if self.direction == EAST:
                    self._x_pos += 1
                case "A" if self.direction == WEST:
                    self._x_pos -= 1
