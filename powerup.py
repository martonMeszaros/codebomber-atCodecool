"""Skeleton file for powerups. Needs major rework."""
# import sdl2
import sdl2.ext

from common import Data


class PowerupData(object):
    """Handle data associated with a powerup."""
    def __init__(self):
        # super(PowerupData, self).__init__()
        self.type = None


class Powerup(sdl2.ext.Entity):
    """."""
    remaining_powerups = []

    def reset_remaining_powerups():
        for i in range(Data.n_of_powerups_per_type_per_player * Data.n_of_players):
            Powerup.remaining_powerups.append(Data.powerup_bombcount)
            Powerup.remaining_powerups.append(Data.powerup_power)
            Powerup.remaining_powerups.append(Data.powerup_speed)
