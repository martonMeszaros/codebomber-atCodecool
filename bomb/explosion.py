"""."""
import sdl2.ext

from common import Color
from game_sys.game_config import config
from game_sys.movement import DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT

DIR_ALL = 4


class ExplosionData(object):
    """."""
    def __init__(self):
        """."""
        # Explosion should stay for 0.5 seconds
        self.fallout = 0.5

    def __eq__(self, other):
        return isinstance(other, ExplosionData)


class Explosion(sdl2.ext.Entity):
    """."""
    def __init__(self, world, sprite_factory, pos, power, direction=DIR_ALL):
        """."""
        if direction == DIR_ALL:
            filename = "assets/explosion_cross.png"
        elif power > 0:
            if direction in (DIR_UP, DIR_DOWN):
                filename = "assets/explosion_vertical.png"
            else:
                filename = "assets/explosion_horizontal.png"
        elif direction == DIR_UP:
                filename = "assets/explosion_top.png"
        elif direction == DIR_RIGHT:
                filename = "assets/explosion_right.png"
        elif direction == DIR_DOWN:
                filename = "assets/explosion_bottom.png"
        elif direction == DIR_LEFT:
                filename = "assets/explosion_left.png"
        self.sprite = sprite_factory.from_image(filename)
        self.sprite.position = pos
        self.sprite.depth = 1
        self.explosiondata = ExplosionData()
        if power > 0:
            if direction == DIR_ALL:
                Explosion(
                    world, sprite_factory,
                    (pos[0], pos[1] - config.sprite_size[1]),
                    power - 1,
                    DIR_UP
                )
                Explosion(
                    world, sprite_factory,
                    (pos[0] + config.sprite_size[0], pos[1]),
                    power - 1,
                    DIR_RIGHT
                )
                Explosion(
                    world, sprite_factory,
                    (pos[0], pos[1] + config.sprite_size[1]),
                    power - 1,
                    DIR_DOWN
                )
                Explosion(
                    world, sprite_factory,
                    (pos[0] - config.sprite_size[0], pos[1]),
                    power - 1,
                    DIR_LEFT
                )
            else:
                if direction == DIR_UP:
                    new_pos = (pos[0], pos[1] - config.sprite_size[1])
                elif direction == DIR_RIGHT:
                    new_pos = (pos[0] + config.sprite_size[0], pos[1])
                elif direction == DIR_DOWN:
                    new_pos = (pos[0], pos[1] + config.sprite_size[1])
                elif direction == DIR_LEFT:
                    new_pos = (pos[0] - config.sprite_size[0], pos[1])
                Explosion(
                    world, sprite_factory,
                    new_pos,
                    power - 1,
                    direction
                )
