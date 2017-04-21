import sdl2
import sdl2.ext
from common import *
import random
from powerup import Powerup


class WallData(object):
    def __init__(self, is_powerup=False):
        # super(WallData, self).__init__()
        self.is_powerup = is_powerup


class Wall(sdl2.ext.Entity):
    sizex = 32
    sizey = 32
    destroyable_walls = []

    def __init__(self, world, sprite, x=0, y=0, is_powerup=False):
        self.sprite = sprite
        self.sprite.x = x
        self.sprite.y = y
        self.walldata = WallData(is_powerup)


def gen_permawall(world, window, sprite_factory):
    # Generate outer walls
    for y in range(0, window.size[1] // Wall.sizey):
        for x in range(0, window.size[0] // Wall.sizex):
            if (
                    x == 0 or y == 0 or
                    x == window.size[0] // Wall.sizex - 1 or
                    y == window.size[1] // Wall.sizey - 1):
                wall_sprite = sprite_factory.from_color(WALL_PERMANENT, (Wall.sizex, Wall.sizey))
                Wall(world, wall_sprite, x * Wall.sizex, y * Wall.sizey)

    # Generate inner walls
    for y in range(0, window.size[1] // Wall.sizey):
        for x in range(0, window.size[0] // Wall.sizex):
            if x % 2 == 1 and y % 2 == 1:
                wall_sprite = sprite_factory.from_color(WALL_PERMANENT, (Wall.sizex, Wall.sizey))
                Wall(world, wall_sprite, x * Wall.sizex + Wall.sizex, y * Wall.sizey + Wall.sizey)


def gen_wall(world, window, sprite_factory, num_of_players):
    walls = []
    walls_to_remove = []
    holes_remaining = 20

    # Generate wall on every empty space
    for y in range(1, window.size[1] // Wall.sizey - 1):
        for x in range(1, window.size[0] // Wall.sizex - 1):
            if not (x % 2 == 0 and y % 2 == 0):
                wall_sprite = sprite_factory.from_color(WALL, (Wall.sizex, Wall.sizey))
                walls.append(Wall(world, wall_sprite, x * Wall.sizex, y * Wall.sizey))

    # Remove walls from starter positions
    player_starter_positions = [
        # First player starting pos
        (32, 32),
        (64, 32),
        (32, 64),
        # Second player starting pos
        (416, 352),
        (384, 352),
        (416, 320)
    ]
    if num_of_players > 2:
        player_starter_positions.append((32, 352))
        player_starter_positions.append((64, 352))
        player_starter_positions.append((32, 320))
        if num_of_players > 3:
            player_starter_positions.append((416, 32))
            player_starter_positions.append((384, 32))
            player_starter_positions.append((416, 64))
    for wall in walls:
        if wall.sprite.position in player_starter_positions:
            wall.delete()
            walls_to_remove.append(wall)

    # remove random walls
    remove_chance = round(holes_remaining / len(walls) * 10) * 2
    while holes_remaining > 0:
        for wall in walls:
            destroy = True if random.randint(0, remove_chance) == 0 else False
            if destroy and holes_remaining > 0:
                wall.delete()
                walls_to_remove.append(wall)
                holes_remaining -= 1

    # Remove deleted walls from the list walls
    for wall in walls_to_remove:
        for wall2 in walls:
            if wall == wall2:
                walls.remove(wall)

    for wall in walls:
        Wall.destroyable_walls.append(wall)


def gen_powerup(world, window, sprite_factory, walls):
    Powerup.fill_powerups()
    walls = walls
    upgrade_chance = round(len(Powerup.remaining_powerups) / len(walls) * 10) * 2
    while len(Powerup.remaining_powerups) > 0:
        for wall in walls:
            if (
                    random.randint(0, len(Powerup.remaining_powerups)) == 0 and
                    len(Powerup.remaining_powerups) > 0 and
                    not wall.walldata.is_powerup):
                # print("num of rem powerups: %s" % len(Powerup.remaining_powerups))
                prev_pos = wall.sprite.position
                powerup = random.choice(Powerup.remaining_powerups)
                Powerup.remaining_powerups.remove(powerup)
                wall = Wall(
                    world,
                    sprite_factory.from_color(POWERUP, (Wall.sizex, Wall.sizey)),
                    prev_pos[0], prev_pos[1],
                    powerup
                )
                # print("placed powerup at {}".format(wall.sprite.position))
                if len(Powerup.remaining_powerups) < 1:
                    break


def generate_step(world, window, sprite_factory, num_of_players=2, step=0):
    if step == 0:
        if len(Wall.destroyable_walls) > 0:
            for wall in Wall.destroyable_walls:
                wall.delete()
            Wall.destroyable_walls = []
        gen_permawall(world, window, sprite_factory)
    elif step == 1:
        gen_wall(world, window, sprite_factory, num_of_players)
    elif step == 2:
        gen_powerup(world, window, sprite_factory, Wall.destroyable_walls)


def generate_map(world, window, sprite_factory, num_of_players=2):
    for wall in Wall.destroyable_walls:
        wall.delete()
    Wall.destroyable_walls = []
    gen_permawall(world, window, sprite_factory)
    gen_wall(world, window, sprite_factory, num_of_players, )
    gen_powerup(world, window, sprite_factory, Wall.destroyable_walls)
