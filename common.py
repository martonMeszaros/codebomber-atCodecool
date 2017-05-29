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