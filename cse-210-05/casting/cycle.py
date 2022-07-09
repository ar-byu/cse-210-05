import constants
from casting.actor import Actor
from shared.point import Point
from datetime import datetime, timedelta

class Cycle(Actor):
    """
    A bike.
    
    The responsibility of Cycle is to move itself.

    """
    def __init__(self, color, position):
        super().__init__()
        self._segments = []
        self._color = color
        self._reset_growth_timer()
        self._prepare_body(position)

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)
        self._check_growth_timer()

    def get_head(self):
        return self._segments[0]

    def _reset_growth_timer(self):
        # Checks time since last growth and resets if >= 15
        now = datetime.now()
        self._growth_timer = now + timedelta(seconds = constants.TIMER)

    def _check_growth_timer(self):
        # Checks the timer. If current time is after the timer, grow tail and reset timer
        now = datetime.now()
        
        if now >= self._growth_timer:
            self.grow_tail(1)
            self._reset_growth_timer()


    def grow_tail(self, number_of_segments):
        # Grows the cycle's tail
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, point):
        # Initializes the player character's body
        x = (point.get_x() * constants.CELL_SIZE)
        y = (point.get_y() * constants.CELL_SIZE)

        for i in range(constants.LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "@" if i == 0 else "#"
            color = self._color

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)