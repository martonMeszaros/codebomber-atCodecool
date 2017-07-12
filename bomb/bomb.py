"""."""
import sdl2.ext


class BombData(object):
    """."""
    def __init__(self, power=0, timer=0, player=None):
        """."""
        self.power = power
        self.timer = timer
        self.player = player

    def __eq__(self, other):
        return isinstance(other, BombData)


class Bomb(sdl2.ext.Entity):
    """."""
    def __init__(self, world, sprite, pos, power, player, timer=3000):
        """."""
        self.sprite = sprite
        self.sprite.position = pos
        self.sprite.depth = 1
        self.bombdata = BombData(power, timer, player)
