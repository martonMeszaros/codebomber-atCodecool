"""System utilized by the game world.
Might need to split into different files.
"""
# import sdl2
import sdl2.ext

from common import Color


class RenderSystem(sdl2.ext.SoftwareSpriteRenderSystem):
    """Used to render every component (entity) in a world."""
    def __init__(self, window):
        super().__init__(window)

    def render(self, components):
        sdl2.ext.fill(self.surface, Color.grass)
        super().render(components)
