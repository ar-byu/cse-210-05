import constants
from scripting.action import Action
from shared.point import Point

class ControlPlayerAction(Action):
    def __init__(self, keyboard_service, up, down, left, right, cast, player):
        """Constructs a new ControlPlayersAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0, constants.CELL_SIZE)
        self._up = up
        self._down = down
        self._left = left
        self._right = right
        self._player = player

    def execute(self, cast, script):
        # left
        if self._keyboard_service.is_key_down(self._left):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down(self._right):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down(self._up):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down(self._down):
            self._direction = Point(0, constants.CELL_SIZE)

        cycle = cast.get_first_actor(self._player)
        cycle.turn_head(self._direction)