from scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        points = cast.get_first_actor("points")
        p1_score = cast.get_first_actor("p1_score")
        p2_score = cast.get_first_actor("p2_score")
        cycle_1 = cast.get_first_actor("player_1")
        segments_1 = cycle_1.get_segments()
        messages_1 = cast.get_actors("messages")
        cycle_2 = cast.get_first_actor("player_2")
        segments_2 = cycle_2.get_segments()
        messages_2 = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(points)
        self._video_service.draw_actors(segments_1)
        self._video_service.draw_actors(messages_1, True)
        self._video_service.draw_actors(segments_2)
        self._video_service.draw_actor(p1_score)
        self._video_service.draw_actor(p2_score)
        self._video_service.draw_actors(messages_2, True)
        self._video_service.flush_buffer()