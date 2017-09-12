"""Commonly used variables and functions."""
# import sdl2
import sdl2.ext

from game_sys.collision.circle_collision_mesh import CircleMesh


def intersects(one, two):
    if isinstance(one, CircleMesh):
        if isinstance(two, CircleMesh):
            xdist = abs(one.x() - two.x())
            ydist = abs(one.y() - two.y())
            sqdist = xdist ** 2 + ydist ** 2
            return sqdist <= (one.r + two.r) ** 2
        else:
            return diffintersects(one, two)
    else:
        if isinstance(two, CircleMesh):
            return diffintersects(two, one)
        else:
            return not (
                (one.bottom() < two.top()) or
                (one.top() > two.bottom()) or
                (one.left() > two.right()) or
                (one.right() < two.left()))


def diffintersects(circle, rect):
    closestX = clamp(circle.x(), rect.left(), rect.right())
    closestY = clamp(circle.y(), rect.top(), rect.bottom())
    distX = circle.x() - closestX
    distY = circle.y() - closestY

    distSQ = distX ** 2 + distY ** 2
    return distSQ < circle.r ** 2


def clamp(value, minV, maxV):
    if value < minV:
        return minV
    elif value > maxV:
        return maxV
    else:
        return value


class Color(object):
    """Contains sdl2.ext Color objects with colors
    defined in google's material design.
    https://material.io/guidelines/style/color.html#color-color-tool
    """
    black = sdl2.ext.Color(0, 0, 0)  # Black
    grass = sdl2.ext.Color(76, 175, 80)  # Green 500
    player = sdl2.ext.Color(255, 255, 0)  # Yellow
    powerup_bombcount = sdl2.ext.Color(55, 71, 79)  # Blue Grey 800
    powerup_power = sdl2.ext.Color(255, 152, 0)  # Orange 500
    powerup_speed = sdl2.ext.Color(3, 169, 244)  # Light Blue 500
    wall = sdl2.ext.Color(189, 189, 189)  # Grey 400
    wall_permanent = sdl2.ext.Color(117, 117, 117)  # Grey 600
    exploseion = sdl2.ext.Color(225, 0, 0)  # Crimson
