import sdl2.ext


class Floor(sdl2.ext.Entity):
    def __init__(self, world, sprite):
        self.sprite = sprite
        self.sprite.position = 0, 0
        self.sprite.depth = -1
