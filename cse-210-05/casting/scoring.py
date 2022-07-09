from casting.actor import Actor
from shared.point import Point
import constants

class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, name, position):
        super().__init__()
        self._points = 0
        self._position = position
        self._name = name
        self.add_points(0)
        self._prepare_banner(position)

    def _prepare_banner(self, position):
        x = (position.get_x() * constants.CELL_SIZE)
        y = (position.get_y() * constants.CELL_SIZE)

        position = x * constants.CELL_SIZE, y * constants.CELL_SIZE
        text = self.set_text(f"{self._name}: {self._points}")

        banner = Actor()
        banner.set_position(position)
        banner.set_text(text)
        banner.set_color(constants.WHITE)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"{self._name}: {self._points}")