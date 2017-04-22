"""Skeleton file for powerups. Needs major rework."""
# import sdl2
import sdl2.ext


class PowerupData(object):
    """Handle data associated with a powerup."""
    def __init__(self):
        self.type = None


class Powerup(sdl2.ext.Entity):
    bombcount = 0
    power = 1
    speed = 2

    n_of_powerups = 6
    remaining_powerups = []

    def reset_remaining_powerups():
        for i in range(Powerup.n_of_powerups):
            Powerup.remaining_powerups.append(Powerup.bombcount)
            Powerup.remaining_powerups.append(Powerup.power)
            Powerup.remaining_powerups.append(Powerup.speed)
