class Powerup(object):
    remaining_powerups = []

    def fill_powerups():
        trollface = []
        for i in range(6):
            trollface.append("firepower")
            trollface.append("bomb_count")
            trollface.append("speed")
        Powerup.remaining_powerups = trollface
