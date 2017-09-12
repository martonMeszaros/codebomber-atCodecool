import sdl2.ext
from game_sys.game_config import config
from game_sys.collision.complex_collision_mesh import ComplexMesh
from game_sys.collision.rectangle_collision_mesh import RectangleMesh


class WallData(object):
    """."""

    def __init__(self, powerup_type):
        """."""
        # super(WallData, self).__init__()
        self.powerup_type = powerup_type


class Wall(sdl2.ext.Entity):
    """."""
    destroyable_walls = []

    def __init__(self, world, sprite, position, powerup_type=None):
        """."""
        self.sprite = sprite
        self.sprite.position = position
        self.sprite.depth = 0
        self.walldata = WallData(powerup_type)
        self.complexmesh = ComplexMesh()
        self.complexmesh.add_mesh(RectangleMesh(0, 0, *config.sprite_size))
