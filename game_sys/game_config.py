import json

import sdl2

config = None


class GameConfig(object):
    def __init__(self, settings_file):
        with open(settings_file) as open_file:
            self.settings = json.load(open_file)
        for player in ["player1", "player2", "player3", "player4"]:
            if self.settings.get(player) is not None:
                for key in self.settings[player]:
                    self.settings[player][key] = sdl2.SDL_GetKeyFromName(bytes(self.settings[player][key], "utf-8"))
        self.window_size = self.settings.get("window_size")
        self.map_size = [15, 13]  # This includes outer walls
        self.sprite_size = (32, 32)
        self.number_of_players = 2
        self.number_of_powerups_per_type_per_player = 3
        self.number_of_random_holes = 9

    def save_settings(self, settings_file):
        # SDL_GetKeyName(SDL_KeyCode).decode("utf-8")
        pass


if __name__ == "game_sys.game_config" and config is None:
    config = GameConfig("assets/settings.json")
