"""Commonly used variables and functions."""
# import sdl2
import sdl2.ext


class Color(object):
    """Contains sdl2.ext Color objects with colors
    defined in google's material design.
    https://material.io/guidelines/style/color.html#color-color-tool
    """
    black = sdl2.ext.Color(0, 0, 0)                 # Black
    grass = sdl2.ext.Color(76, 175, 80)             # Green 500
    powerup_bombcount = sdl2.ext.Color(55, 71, 79)  # Blue Grey 800
    powerup_power = sdl2.ext.Color(255, 152, 0)     # Orange 500
    powerup_speed = sdl2.ext.Color(3, 169, 244)     # Light Blue 500
    wall = sdl2.ext.Color(189, 189, 189)            # Grey 400
    wall_permanent = sdl2.ext.Color(117, 117, 117)  # Grey 600


class Data(object):
    """Stores data to fix import issues when files import each other."""
    map_size = (15, 13)
    n_of_players = 2
    n_of_powerups_per_type_per_player = 3
    n_of_random_holes = 9
    # Powerup types can't start with 0, because
    # this data is used to check if a powerup should
    # spawn when blowing up a wall.
    powerup_bombcount = 1
    powerup_power = 2
    powerup_speed = 3
    sprite_size = (32, 32)

    def __set_map_size(x, y):
        pass

    def set_sprite_size(n):
        """Set Data.sprite_size to (n, n)"""
        Data.sprite_size = (n, n)
