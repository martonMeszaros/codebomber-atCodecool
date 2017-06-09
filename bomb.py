"""."""
import sdl2.ext
from velocity import Velocity


class BombData(object):
    """."""
    def __init__(self, power, timer, position):
        """."""
        # super(BombData, self).__init__()
        self.power = power
        self.timer = timer
        self.position = position


class Bomb(sdl2.ext.Entity):
    """."""
    def __init__(self, world, sprite, pos, power, timer=3000):
        """."""
        self.sprite = sprite
        self.sprite.position = pos
        self.bombdata = BombData(power, timer, pos)
        self.velocity = Velocity()
