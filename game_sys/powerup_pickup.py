import sdl2.ext

from game_sys.grid_coordinates import snap_to_grid
from player.player_data import PlayerData
from map_components.wall import WallData
from map_components.powerup import ID_SPEED, ID_POWER, ID_BOMBCOUNT


class PickupPowerup(sdl2.ext.Applicator):
    def __init__(self):
        super(PickupPowerup, self).__init__()
        self.componenttypes = PlayerData, sdl2.ext.Sprite

    def process(self, world, componentsets):
        walls = world.get_entities(WallData(None))
        for playerdata, sprite in componentsets:
            for wall in walls:
                if snap_to_grid(*wall.sprite.position) == snap_to_grid(*sprite.position) and wall.walldata.powerup_type is not None:
                    if wall.walldata.powerup_type == ID_SPEED:
                        playerdata.speed += 1
                    elif wall.walldata.powerup_type == ID_BOMBCOUNT:
                        playerdata.bombcount += 1
                    elif wall.walldata.powerup_type == ID_POWER:
                        playerdata.power += 1
                    walls.remove(wall)
                    wall.delete()
                    break
