import sdl2.ext


class WallData(object):
    """."""

    def __init__(self, powerup_type):
        """."""
        # super(WallData, self).__init__()
        self.powerup_type = powerup_type

    def __eq__(self, other):
        return isinstance(other, WallData)


class Wall(sdl2.ext.Entity):
    """."""
    destroyable_walls = []

    def __init__(self, world, sprite, position, powerup_type=None):
        """."""
        self.sprite = sprite
        self.sprite.position = position
        self.sprite.depth = 0
        self.walldata = WallData(powerup_type)
