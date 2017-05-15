"""."""
import sdl2.ext


class ExplosionData(object):
    """."""
    def __init__(self, power, direction):
        """."""
        # super(ExplosionData, self).__init__()
        self.power = power
        self.direction = direction


class Explosion(sdl2.ext.Entity):
    """."""
    dir_up = 0
    dir_right = 1
    dir_down = 2
    dir_left = 3

    def __init__(self, sprite, pos, power, direction):
        """."""
        self.sprite = sprite
        self.sprite.position = pos
        self.explosiondata = ExplosionData(power, direction)
