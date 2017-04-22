"""."""
import random

# import sdl2
import sdl2.ext

from common import Color
from powerup import Powerup


class WallData(object):
    """."""
    def __init__(self, is_powerup):
        """."""
        # super(WallData, self).__init__()
        self.is_powerup = is_powerup


class Wall(sdl2.ext.Entity):
    """."""
    n_to_remove = 9
    size = (48, 48)
    destroyable_walls = []

    def __init__(self, world, sprite, posx=0, posy=0, is_powerup=False):
        """."""
        self.sprite = sprite
        self.sprite.position = posx, posy
        self.walldata = WallData(is_powerup)


class GenerateWalls(object):
    """Holds all functions of generating a map."""
    n_of_steps = 5
    step = 1

    def gen_permawalls(world, window, sprite_factory):
        """Generate outer and inner walls that can't be destroyed."""
        # Compensate for coords starting with 0
        offset = 1

        # Generate outer walls
        for y in range(0, window.size[1] // Wall.size[1]):
            for x in range(0, window.size[0] // Wall.size[0]):
                if (
                        # Top most or left most walls
                        x == 0 or y == 0 or
                        # Right most walls
                        x == window.size[0] // Wall.size[0] - offset or
                        # Bottom most walls
                        y == window.size[1] // Wall.size[1] - offset):
                    wall_sprite = sprite_factory.from_color(
                        Color.wall_permanent, (Wall.size[0], Wall.size[1])
                    )
                    Wall(world, wall_sprite, x * Wall.size[0], y * Wall.size[1])

        # Generate inner walls
        for y in range(offset, window.size[1] // Wall.size[1] - (offset*2)):
            for x in range(offset, window.size[0] // Wall.size[0] - (offset*2)):
                # Only at every second x and y coordinate
                if x % 2 == 0 and y % 2 == 0:
                    wall_sprite = sprite_factory.from_color(
                        Color.wall_permanent, (Wall.size[0], Wall.size[1]))
                    Wall(world, wall_sprite, x * Wall.size[0], y * Wall.size[1])

    def gen_wall(world, window, sprite_factory):
        """Generate destroyable walls in every blank space."""
        offset = 1

        # Generate wall on every empty space
        for y in range(offset, window.size[1] // Wall.size[1] - offset):
            for x in range(offset, window.size[0] // Wall.size[0] - offset):
                if not (x % 2 == 0 and y % 2 == 0):
                    wall_sprite = sprite_factory.from_color(
                        Color.wall, (Wall.size[0], Wall.size[1]))
                    Wall.destroyable_walls.append(
                        Wall(world, wall_sprite, x * Wall.size[0], y * Wall.size[1]))

    def remove_from_playerpos(n_of_players):
        """Remove 3 walls from every players starting position."""
        # At least 2 players are always playing.
        # Should be made scalable with different size of map layouts.
        playerpos = [
            (1 * Wall.size[0], 1 * Wall.size[1]),
            (1 * Wall.size[0], 2 * Wall.size[1]),
            (2 * Wall.size[0], 1 * Wall.size[1]),
            (13 * Wall.size[0], 11 * Wall.size[1]),
            (13 * Wall.size[0], 10 * Wall.size[1]),
            (12 * Wall.size[0], 11 * Wall.size[1])
        ]
        if n_of_players > 2:
            playerpos.append(
                (13 * Wall.size[0], 1 * Wall.size[1]))
            playerpos.append(
                (13 * Wall.size[0], 2 * Wall.size[1]))
            playerpos.append(
                (12 * Wall.size[0], 1 * Wall.size[1]))
            if n_of_players > 3:
                playerpos.append(
                    (1 * Wall.size[0], 11 * Wall.size[1]))
                playerpos.append(
                    (1 * Wall.size[0], 10 * Wall.size[1]))
                playerpos.append(
                    (2 * Wall.size[0], 11 * Wall.size[1]))

        walls_to_remove = []
        # Check wall positions in Wall.destroyable_walls
        for wall in Wall.destroyable_walls:
            if wall.sprite.position in playerpos:
                walls_to_remove.append(wall)

        for wall in walls_to_remove:
            Wall.destroyable_walls.remove(wall)
            wall.delete()

    def remove_from_random():
        """Remove walls from random positions."""
        for i in range(Wall.n_to_remove):
            selected_wall = random.choice(Wall.destroyable_walls)
            Wall.destroyable_walls.remove(selected_wall)
            selected_wall.delete()

    def gen_powerup(world, window, sprite_factory):
        """Replace some of the remaining walls with powerups."""
        Powerup.reset_remaining_powerups()
        new_walls = []

        while len(Powerup.remaining_powerups) > 0:
            selected_wall = random.choice(Wall.destroyable_walls)
            Wall.destroyable_walls.remove(selected_wall)
            # Save the position of the wall
            position = selected_wall.sprite.position
            selected_wall.delete()
            # Select a powerup type from the remaining
            powerup_type = random.choice(Powerup.remaining_powerups)
            Powerup.remaining_powerups.remove(powerup_type)
            # Set proper sprite color - temporary
            if powerup_type == Powerup.bombcount:
                wall_sprite = sprite_factory.from_color(
                    Color.powerup_bombcount, (Wall.size[0], Wall.size[1]))
            elif powerup_type == Powerup.power:
                wall_sprite = sprite_factory.from_color(
                    Color.powerup_power, (Wall.size[0], Wall.size[1]))
            elif powerup_type == Powerup.speed:
                wall_sprite = sprite_factory.from_color(
                    Color.powerup_speed, (Wall.size[0], Wall.size[1]))
            # Create the new wall
            new_walls.append(
                Wall(world, wall_sprite, position[0], position[1], powerup_type))

        for wall in new_walls:
            Wall.destroyable_walls.append(wall)

    def generate_step(world, window, sprite_factory, n_of_players=2):
        """Execute a single phase of map generation."""
        if GenerateWalls.step == 1:
            if len(Wall.destroyable_walls) > 0:
                for wall in Wall.destroyable_walls:
                    wall.delete()
                Wall.destroyable_walls = []
            GenerateWalls.gen_permawalls(world, window, sprite_factory)
        elif GenerateWalls.step == 2:
            GenerateWalls.gen_wall(world, window, sprite_factory)
        elif GenerateWalls.step == 3:
            GenerateWalls.remove_from_playerpos(n_of_players)
        elif GenerateWalls.step == 4:
            GenerateWalls.remove_from_random()
        elif GenerateWalls.step == 5:
            GenerateWalls.gen_powerup(world, window, sprite_factory)

        if GenerateWalls.step < GenerateWalls.n_of_steps:
            GenerateWalls.step += 1
        else:
            GenerateWalls.step = 1

    def generate_map(world, window, sprite_factory, n_of_players=2):
        """Execute all steps of world generation."""
        for wall in Wall.destroyable_walls:
            wall.delete()
        Wall.destroyable_walls = []
        GenerateWalls.gen_permawalls(world, window, sprite_factory)
        GenerateWalls.gen_wall(world, window, sprite_factory)
        GenerateWalls.remove_from_playerpos(n_of_players)
        GenerateWalls.remove_from_random()
        GenerateWalls.gen_powerup(world, window, sprite_factory)
