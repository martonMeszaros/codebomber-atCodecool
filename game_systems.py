import sdl2
import sdl2.ext

from common import *


class RenderSystem(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super().__init__(window)

    def render(self, components):
        sdl2.ext.fill(self.surface, GRASS_COLOR)
        super().render(components)
