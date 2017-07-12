"""."""
import sdl2.ext

import game_sys.movement
from player.player_data import PlayerData
from game_sys.game_config import config
from game_sys.grid_coordinates import grid_pos, snap_to_grid
from game_sys.controls import Controls
from bomb.bomb import BombData, Bomb
from common import Color


class Player(sdl2.ext.Entity):
    """."""

    def __init__(self, world, sprite, is_ai=False):
        """."""
        self.sprite = sprite
        self.sprite.depth = 2
        self.playerdata = PlayerData(is_ai)
        self.sprite.position = get_starting_position(self.playerdata.number)
        self.movement = game_sys.movement.Movement(get_starting_position(self.playerdata.number))
        self.controls = Controls(self.playerdata.number)

    def movement_pressed(self, key):
        if self.controls.movement[key] not in self.movement.active_directions:
            self.movement.active_directions.append(self.controls.movement[key])

    def movement_released(self, key):
        self.movement.active_directions.remove(self.controls.movement[key])

    def place_bomb(self, world, sprite_factory):
        if self.playerdata.bombs_placed < self.playerdata.bombcount:
            bombs = world.get_entities(BombData())
            valid_position = True
            for bomb in bombs:
                print(bomb.sprite.position)
                if bomb.sprite.position == snap_to_grid(*self.sprite.position):
                    valid_position = False
                    break
            if valid_position:
                self.playerdata.bombs_placed += 1
                Bomb(world,
                     sprite_factory.from_color(Color.black, config.sprite_size),
                     snap_to_grid(*self.sprite.position),
                     self.playerdata.power,
                     self)


def get_starting_position(player_number):
    if player_number == 1:
        return grid_pos(1, 1)
    elif player_number == 2:
        return grid_pos(config.map_size[0] - 2, config.map_size[1] - 2)
    elif player_number == 3:
        return grid_pos(config.map_size[0] - 2, 1)
    elif player_number == 4:
        return grid_pos(1, config.map_size[1] - 2)
