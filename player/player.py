"""."""
import sdl2.ext

import player.movement
from player.player_data import PlayerData
from game_sys.game_config import config
from game_sys.grid_coordinates import grid_pos
from player.controls import Controls


class Player(sdl2.ext.Entity):
    """."""
    def __init__(self, world, sprite, is_ai=False):
        """."""
        self.sprite = sprite
        self.sprite.depth = 2
        self.playerdata = PlayerData(is_ai)
        self.sprite.position = get_starting_position(self.playerdata.number)
        self.movement = player.movement.Movement(get_starting_position(self.playerdata.number))
        self.controls = Controls(self.playerdata.number)

    def movement_pressed(self, key):
        if self.controls.movement[key] not in self.movement.active_directions:
            self.movement.active_directions.append(self.controls.movement[key])

    def movement_released(self, key):
        self.movement.active_directions.remove(self.controls.movement[key])

    def place_bomb(self):
        pass


def get_starting_position(player_number):
    if player_number == 1:
        return grid_pos(1, 1)
    elif player_number == 2:
        return grid_pos(config.map_size[0] - 2, config.map_size[1] - 2)
    elif player_number == 3:
        return grid_pos(config.map_size[0] - 2, 1)
    elif player_number == 4:
        return grid_pos(1, config.map_size[1] - 2)
