"""."""
import sdl2.ext


class BombData(object):
    """."""
    def __init__(self, power, timer):
        """."""
        # super(BombData, self).__init__()
        self.power = power
        self.timer = timer


class Bomb(sdl2.ext.Entity):
    """."""
    def __init__(self, sprite, pos, power, timer=3000):
        """."""
        self.sprite = sprite
        self.sprite.position = pos
        self.bombdata = BombData(power, timer)
