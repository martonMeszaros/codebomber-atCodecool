"""."""
import sdl2.ext


class Player(sdl2.ext.Entity):
    """."""
    def __init__(self, world, sprite, pos, controls, is_ai=False):
        """."""
        self.sprite = sprite
        self.sprite.position = pos
        self.playerdata = PlayerData(controls, is_ai)
