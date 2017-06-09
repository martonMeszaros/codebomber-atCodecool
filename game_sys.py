"""System utilized by the game world.
Might need to split into different files.
"""
import json
import threading

import sdl2
import sdl2.ext

from common import Color
from velocity import Velocity
from bomb import BombData

config = None


class RenderSystem(sdl2.ext.SoftwareSpriteRenderSystem):
    """Used to render every component (entity) in a world."""

    def __init__(self, window):
        super().__init__(window)

    def render(self, components):
        sdl2.ext.fill(self.surface, Color.grass)
        super().render(components)


class GameConfig(object):

    def __init__(self, settings_file):
        with open(settings_file) as open_file:
            self.settings = json.load(open_file)
        for player in ["player1", "player2", "player3", "player4"]:
            if self.settings.get(player) is not None:
                for key in self.settings[player]:
                    self.settings[player][key] = sdl2.SDL_GetKeyFromName(bytes(self.settings[player][key], "utf-8"))
        self.map_size = [15, 13]  # This includes outer walls
        self.sprite_size = (32, 32)
        self.number_of_players = 2
        self.number_of_powerups_per_type_per_player = 3
        self.number_of_random_holes = 9

    def save_settings(self, settings_file):
        # SDL_GetKeyName(SDL_KeyCode).decode("utf-8")
        pass


class BombMovementTest(sdl2.ext.Applicator):

    def __init__(self):
        self.componenttypes = (Velocity, sdl2.ext.sprite.SoftwareSprite, BombData)
        self.is_applicator = True

    def process(self, world, componentsets):
        delta_time = world.delta_time
        for vel, sprite, bdata in componentsets:
            velocity = vel.get_velocity()
            old_position = bdata.position
            new_position = (
                old_position[0] + (velocity[0] * config.sprite_size[0] * delta_time),
                old_position[1] + (velocity[1] * config.sprite_size[1] * delta_time)
            )
            bdata.position = new_position
            sprite.position = round(new_position[0]), round(new_position[1])

if __name__ == "game_sys" and config is None:
    config = GameConfig("settings.json")
