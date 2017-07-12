from game_sys.game_config import config
import game_sys.movement as movement


class Controls(object):
    def __init__(self, player_number):
        keys = config.settings["player{}".format(player_number)]
        self.movement = {
            keys["key_up"]: movement.DIR_UP,
            keys["key_right"]: movement.DIR_RIGHT,
            keys["key_down"]: movement.DIR_DOWN,
            keys["key_left"]: movement.DIR_LEFT
        }
        self.bomb_placement = keys["key_bomb"]
