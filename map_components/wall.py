"""."""
import random

# import sdl2
import sdl2.ext

from common import Color
from game_sys.game_config import config
from game_sys.grid_coordinates import grid_pos, get_map_size
import map_components.powerup


class WallData(object):
    """."""

    def __init__(self, powerup_type):
        """."""
        # super(WallData, self).__init__()
        self.powerup_type = powerup_type


class Wall(sdl2.ext.Entity):
    """."""
    destroyable_walls = []

    def __init__(self, world, sprite, position, powerup_type=None):
        """."""
        self.sprite = sprite
        self.sprite.position = position
        self.sprite.depth = 0
        self.walldata = WallData(powerup_type)


def __gen_permawalls(world, sprite_factory):
    """Generate outer and inner walls that can't be destroyed."""
    for y in range(config.map_size[1]):
        for x in range(config.map_size[0]):
            # Generate outer walls
            if (
                    # Top most or left most walls
                    x == 0 or y == 0 or
                    # Right most walls
                    x == config.map_size[0] - 1 or
                    # Bottom most walls
                    y == config.map_size[1] - 1):
                wall_sprite = sprite_factory.from_color(Color.wall_permanent, config.sprite_size)
                Wall(world, wall_sprite, (x * config.sprite_size[0], y * config.sprite_size[1]))
            # Generate inner walls
            elif x % 2 == 0 and y % 2 == 0:
                wall_sprite = sprite_factory.from_color(Color.wall_permanent, config.sprite_size)
                Wall(world, wall_sprite, (x * config.sprite_size[0], y * config.sprite_size[1]))


def __gen_wall(world, sprite_factory):
    """Generate destroyable walls in every blank space."""
    offset = 1

    # Generate wall on every empty space
    for y in range(offset, config.map_size[1] - offset):
        for x in range(offset, config.map_size[0] - offset):
            if not (x % 2 == 0 and y % 2 == 0):
                wall_sprite = sprite_factory.from_color(Color.wall, config.sprite_size)
                Wall.destroyable_walls.append(
                    Wall(world, wall_sprite, (x * config.sprite_size[0], y * config.sprite_size[1])))


def __remove_from_playerpos(n_of_players):
    """Remove 3 walls from every players starting position."""
    # At least 2 players are always playing.
    # Should be made scalable with different size of map layouts.
    offset = 2
    playerpos = [
        grid_pos(1, 1),
        grid_pos(1, 2),
        grid_pos(2, 1),
        grid_pos(config.map_size[0] - offset, config.map_size[1] - offset),
        grid_pos(config.map_size[0] - offset, config.map_size[1] - offset - 1),
        grid_pos(config.map_size[0] - offset - 1, config.map_size[1] - offset)
    ]
    if n_of_players > 2:
        playerpos.append(grid_pos(config.map_size[0] - offset, 1))
        playerpos.append(grid_pos(config.map_size[0] - offset, 2))
        playerpos.append(grid_pos(config.map_size[0] - offset - 1, 1))
        if n_of_players > 3:
            playerpos.append(grid_pos(1, config.map_size[1] - offset))
            playerpos.append(grid_pos(2, config.map_size[1] - offset))
            playerpos.append(grid_pos(1, config.map_size[1] - offset - 1))

    walls_to_remove = []
    # Check wall positions in Wall.destroyable_walls
    for wall in Wall.destroyable_walls:
        if wall.sprite.position in playerpos:
            walls_to_remove.append(wall)

    for wall in walls_to_remove:
        Wall.destroyable_walls.remove(wall)
        wall.delete()


def __remove_from_random():
    """Remove walls from random positions."""
    for i in range(config.number_of_random_holes):
        selected_wall = random.choice(Wall.destroyable_walls)
        Wall.destroyable_walls.remove(selected_wall)
        selected_wall.delete()


def __gen_powerup(world, sprite_factory):
    """Replace some of the remaining walls with powerups."""
    map_components.powerup.reset_remaining_powerups()
    new_walls = []

    while len(map_components.powerup.remaining_powerups) > 0:
        selected_wall = random.choice(Wall.destroyable_walls)
        Wall.destroyable_walls.remove(selected_wall)
        # Save the position of the wall
        position = selected_wall.sprite.position
        selected_wall.delete()
        # Select a powerup type from the remaining
        powerup_type = random.choice(map_components.powerup.remaining_powerups)
        map_components.powerup.remaining_powerups.remove(powerup_type)
        # Set proper sprite color - temporary
        if powerup_type == map_components.powerup.ID_BOMBCOUNT:
            wall_sprite = sprite_factory.from_color(Color.powerup_bombcount, config.sprite_size)
        elif powerup_type == map_components.powerup.ID_POWER:
            wall_sprite = sprite_factory.from_color(Color.powerup_power, config.sprite_size)
        elif powerup_type == map_components.powerup.ID_SPEED:
            wall_sprite = sprite_factory.from_color(Color.powerup_speed, config.sprite_size)
        # Create the new wall
        new_walls.append(
            Wall(world, wall_sprite, position, powerup_type))

    for wall in new_walls:
        Wall.destroyable_walls.append(wall)


def generate_map(world, sprite_factory, n_of_players=2):
    """Execute all steps of world generation."""
    for wall in Wall.destroyable_walls:
        wall.delete()
    Wall.destroyable_walls = []
    __gen_wall(world, sprite_factory)
    __remove_from_playerpos(n_of_players)
    __remove_from_random()
    __gen_powerup(world, sprite_factory)
