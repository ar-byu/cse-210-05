import constants
from casting.cast import Cast
from casting.cycle import Cycle
from casting.playerpoints import PlayerPoints
from casting.scoring import Score
from scripting.action_scripts import Script
from scripting.control_player_action import ControlPlayerAction
from scripting.move_actors_action import MoveActorsAction
from scripting.handle_collisions_action import HandleCollisionsAction
from scripting.draw_actors_action import DrawActorsAction
from directing.gamemaster import GameMaster
from services.keyboard_service import KeyboardService
from services.video_service import VideoService
from shared.color import Color
from shared.point import Point

def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("player_1", Cycle(constants.RED, Point(5,5)))
    cast.add_actor("player_2", Cycle(constants.GREEN, Point(15,15)))
    cast.add_actor("points", PlayerPoints())
    cast.add_actor("p1_score", Score("Player 1", Point(0, 0)))
    cast.add_actor("p2_score", Score("Player 2", Point(constants.MAX_X - 100, 0)))
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    # Initializes script needs
    script = Script()
    script.add_action("input", ControlPlayerAction(keyboard_service, 'w', 's', 'a', 'd', cast, 'player_1'))
    script.add_action("input", ControlPlayerAction(keyboard_service, 'i', 'k', 'j', 'l', cast, 'player_2'))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = GameMaster(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()