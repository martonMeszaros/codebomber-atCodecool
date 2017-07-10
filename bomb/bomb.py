"""."""
import sdl2.ext
from player.movement import Movement


class BombData(object):
    """."""
    def __init__(self, power, timer):
        """."""
        # super(BombData, self).__init__()
        self.power = power
        self.timer = timer


class Bomb(sdl2.ext.Entity):
    """."""
    def __init__(self, world, sprite, pos, power, timer=3000):
        """."""
        self.sprite = sprite
        self.sprite.position = pos
        self.sprite.depth = 1
        self.bombdata = BombData(power, timer)
        self.movement = Movement(pos)
