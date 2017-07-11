"""."""
import sdl2.ext

import player.movement
from player.player_data import PlayerData
from game_sys.game_config import config
from player.controls import Controls


class Player(sdl2.ext.Entity):
    """."""
    def __init__(self, world, sprite, is_ai=False):
        """."""
        self.sprite = sprite
        self.sprite.depth = 2
        self.playerdata = PlayerData(is_ai)
        self.sprite.position = config.player_positions[self.playerdata.number - 1]
        self.movement = player.movement.Movement(config.player_positions[self.playerdata.number - 1])
        self.controls = Controls(self.playerdata.number)

    def movement_pressed(self, key):
        if self.controls.movement[key] not in self.movement.active_directions:
            self.movement.active_directions.append(self.controls.movement[key])

    def movement_released(self, key):
        self.movement.active_directions.remove(self.controls.movement[key])

    def place_bomb(self):
        pass
