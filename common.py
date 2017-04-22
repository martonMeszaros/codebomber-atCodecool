"""Constants and commonly used functions."""
# import sdl2
import sdl2.ext


class Color(object):
    """Contains sdl2.ext Color objects with colors
    defined in google's material design.
    """
    grass = sdl2.ext.Color(76, 175, 80)             # Green 500
    wall_permanent = sdl2.ext.Color(117, 117, 117)  # Grey 600
    wall = sdl2.ext.Color(189, 189, 189)            # Grey 400
    black = sdl2.ext.Color(0, 0, 0)                 # Black
    powerup_power = sdl2.ext.Color(255, 197, 3)     # Amber 500
    powerup_bombcount = sdl2.ext.Color(55, 71, 79)  # Blue Grey 800
    powerup_speed = sdl2.ext.Color(3, 169, 244)     # Light Blue 500
