"""."""
import sdl2.ext

import powerup


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

    def __init__(self, controls, is_ai):
        # The commented out line is used in the pong tutorial, not sure why.
        # super(PlayerData, self).__init__()
        self.key_up = controls["key_up"]
        self.key_right = controls["key_right"]
        self.key_down = controls["key_down"]
        self.key_left = controls["key_left"]
        self.key_bomb = controls["key_bomb"]

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
        if powerup_type == powerup.ID_BOMBCOUNT:
            self.bombcount += PlayerData.id_bombcount
        elif powerup_type == powerup.ID_POWER:
            self.power += PlayerData.id_power
        elif powerup_type == powerup.ID_SPEED:
            self.speed += PlayerData.id_speed


class Player(sdl2.ext.Entity):
    """."""
    def __init__(self, world, sprite, pos, controls, is_ai=False):
        """."""
        self.sprite = sprite
        self.sprite.position = pos
        self.playerdata = PlayerData(controls, is_ai)
