"""."""
import sdl2.ext

from common import Data


class PlayerData(object):
    """Handle data associated with a player. This includes:
    Number of bombs a player has, number of placed bombs, their power,
    Players number, speed and whether they are ai controlled.
    The variable naming convention may need to be reworked.
    """
    base_bombcount = 1
    base_power = 2
    base_speed = 1
    powerup_bombcount = 1
    powerup_power = 1
    powerup_speed = 1
    number = 1

    def __init__(self, is_ai):
        # The commented out line is used in the pong tutorial, not sure why.
        # super(PlayerData, self).__init__()
        self.key_up = None
        self.key_right = None
        self.key_down = None
        self.key_left = None
        self.key_bomb = None

        self.bombcount = PlayerData.base_bombcount
        self.bombs_placed = 0
        self.power = PlayerData.base_power
        self.speed = PlayerData.base_speed

        self.is_ai = is_ai
        self.number = PlayerData.number
        PlayerData.number += 1

    def powerup(self, powerup_type):
        """Change one of the players' data depending
        on what kind of powerup they picked up.
        """
        if powerup_type == Data.id_bombcount:
            self.bombcount += PlayerData.id_bombcount
        elif powerup_type == Data.id_power:
            self.power += PlayerData.id_power
        elif powerup_type == Data.id_speed:
            self.speed += PlayerData.id_speed


class Player(sdl2.ext.Entity):
    """."""
    def __init__(self, world, sprite, pos, is_ai=False):
        """."""
        self.sprite = sprite
        self.sprite.position = pos
        self.playerdata = PlayerData(is_ai)
