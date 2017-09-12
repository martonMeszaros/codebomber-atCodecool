import sdl2.ext

from game_sys.collision.complex_collision_mesh import ComplexMesh
from player.player_data import PlayerData
from common import intersects


class Collider(sdl2.ext.Applicator):
    def __init__(self):
        super(Collider, self).__init__()
        self.componenttypes = PlayerData, ComplexMesh, sdl2.ext.Sprite

    def process(self, world, componentsets):
        colliders = world.get_entities(ComplexMesh())
        for player, complex_mesh, sprite in componentsets:
            flag = False
            player_id = id(complex_mesh)
            for collider in colliders:
                if player_id != id(collider.complexmesh):
                    for mesh in complex_mesh.meshes:
                        mesh.transform = sprite.position
                        for other_mesh in collider.complexmesh.meshes:
                            other_mesh.transform = collider.sprite.position
                            if intersects(mesh, other_mesh):
                                print('ááááá')
                                flag = True
                                break
                        if flag:
                            break
                if flag:
                    break
