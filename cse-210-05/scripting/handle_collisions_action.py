import constants
from casting.actor import Actor
from scripting.action import Action
from shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when a cycle gains a point,
    collides with itself or its opponent, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_point_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
    
    def _handle_point_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        p1_score = cast.get_first_actor("p1_score")
        p2_score = cast.get_first_actor("p2_score")
        point = cast.get_first_actor("points")
        cycle_1 = cast.get_first_actor("player_1")
        cycle_2 = cast.get_first_actor("player_2")
        head_1 = cycle_1.get_head()
        head_2 = cycle_2.get_head()

        if head_1.get_position().equals(point.get_position()):
            points = point.get_points()
            p1_score.add_points(points)
            point.reset()
        
        if head_2.get_position().equals(point.get_position()):
            points = point.get_points()
            p2_score.add_points(points)
            point.reset()

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if a cycle collides with one of its segments or its opponent's segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle_1 = cast.get_first_actor("player_1")
        cycle_2 = cast.get_first_actor("player_2")
        head_1 = cycle_1.get_segments()[0]
        head_2 = cycle_2.get_segments()[0]
        segments_1 = cycle_1.get_segments()[1:]
        segments_2 = cycle_2.get_segments()[1:]
        
        for segment in segments_1:
            if head_1.get_position().equals(segment.get_position()) or head_1.get_position().equals(head_2.get_position()):
                self._is_game_over = True

        for segment in segments_2:
            if head_2.get_position().equals(segment.get_position()) or head_2.get_position().equals(head_1.get_position()):
                self._is_game_over = True
        
        for segment, segment in zip(segments_1, segments_2):
            if head_1.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle_1 = cast.get_first_actor("player_1")
            segments_1 = cycle_1.get_segments()
            cycle_2 = cast.get_first_actor("player_2")
            segments_2 = cycle_2.get_segments()
            points = cast.get_first_actor("points")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments_1:
                segment.set_color(constants.WHITE)
            
            for segment in segments_2:
                segment.set_color(constants.WHITE)
            points.set_color(constants.WHITE)