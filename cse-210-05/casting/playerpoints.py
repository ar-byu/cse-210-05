import random
import constants
from casting.actor import Actor
from shared.point import Point


class PlayerPoints(Actor):
    """
    An object that earns a player a point.
    
    The responsibility of PlayerPoints is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "Constructs a new Food."
        super().__init__()
        self._points = 0
        self.set_text("0")
        self.set_color(constants.YELLOW)
        self.reset()
        
    def reset(self):
        """Selects a random position and points that the food is worth."""
        self._points = 1
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        
    def get_points(self):
        """Gets the points the food is worth.
        
        Returns:
            points (int): The points the food is worth.
        """
        return self._points