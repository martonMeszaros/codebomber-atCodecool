import map_components.powerup

BASE_BOMBCOUNT = 1
BASE_POWER = 1
BASE_SPEED = 4
POWERUP_BOMBCOUNT = 1
POWERUP_POWER = 1
POWERUP_SPEED = 1
player_number = 1


class PlayerData(object):
    """Handle data associated with a player. This includes:
    Number of bombs a player has, number of placed bombs, their power,
    Players number, speed and whether they are ai controlled.
    The variable naming convention may need to be reworked.
    """

    def __init__(self, is_ai):
        # The commented out line is used in the pong tutorial, not sure why.
        # super(PlayerData, self).__init__()
        global player_number

        self.bombcount = BASE_BOMBCOUNT
        self.bombs_placed = 0
        self.power = BASE_POWER
        self.speed = BASE_SPEED

        self.is_ai = is_ai
        self.number = player_number
        player_number += 1

    def powerup(self, powerup_type):
        """Change one of the players' data depending
        on what kind of powerup they picked up.
        """
        if powerup_type == powerup.ID_BOMBCOUNT:
            self.bombcount += POWERUP_BOMBCOUNT
        elif powerup_type == powerup.ID_POWER:
            self.power += POWERUP_POWER
        elif powerup_type == powerup.ID_SPEED:
            self.speed += POWERUP_SPEED
