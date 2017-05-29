"""Skeleton file for powerups. Needs major rework."""
# import sdl2
import sdl2.ext

from game_sys import config

ID_BOMBCOUNT = 1
ID_POWER = 2
ID_SPEED = 3

remaining_powerups = []


def reset_remaining_powerups():
    for _ in range(config.number_of_powerups_per_type_per_player * config.number_of_players):
        remaining_powerups.append(ID_BOMBCOUNT)
        remaining_powerups.append(ID_POWER)
        remaining_powerups.append(ID_SPEED)


class PowerupData(object):
    """Handle data associated with a powerup."""
    def __init__(self):
        # super(PowerupData, self).__init__()
        self.type = None


class Powerup(sdl2.ext.Entity):
    pass
