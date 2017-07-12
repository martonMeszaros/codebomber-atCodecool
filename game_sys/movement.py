import math

import sdl2.ext

from game_sys.game_config import config
from player.player_data import PlayerData

DIR_UP = 0
DIR_RIGHT = 1
DIR_DOWN = 2
DIR_LEFT = 3
DIR_VELOCITY_TARGET = (
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
)
ACCELERATION_DIVIDER = 0.15


class Movement(object):
    def __init__(self, position):
        self.velocity = [0, 0]
        self.position = position
        self.active_directions = list()


class PlayerMovement(sdl2.ext.Applicator):
    def __init__(self):
        super(PlayerMovement, self).__init__()
        self.componenttypes = (Movement, PlayerData, sdl2.ext.Sprite)

    def process(self, world, componentsets):
        delta_time = world.delta_time
        for movement, player_data, sprite in componentsets:
            target_velocity_direction = [0, 0]
            for direction in movement.active_directions:
                target_velocity_direction[0] += DIR_VELOCITY_TARGET[direction][0]
                target_velocity_direction[1] += DIR_VELOCITY_TARGET[direction][1]
            target_velocity = (
                target_velocity_direction[0] * player_data.speed,
                target_velocity_direction[1] * player_data.speed
            )
            velocity_delta = [
                target_velocity[0] - movement.velocity[0],
                target_velocity[1] - movement.velocity[1]
            ]
            max_velocity_step = player_data.speed / ACCELERATION_DIVIDER * delta_time
            if math.fabs(velocity_delta[0]) > max_velocity_step:
                velocity_delta[0] = math.copysign(max_velocity_step, velocity_delta[0])
            if math.fabs(velocity_delta[1]) > max_velocity_step:
                velocity_delta[1] = math.copysign(max_velocity_step, velocity_delta[1])
            movement.velocity[0] += velocity_delta[0]
            movement.velocity[1] += velocity_delta[1]
            old_position = movement.position
            new_position = (
                old_position[0] + (movement.velocity[0] * config.sprite_size[0] * delta_time),
                old_position[1] + (movement.velocity[1] * config.sprite_size[1] * delta_time)
            )
            movement.position = new_position
            sprite.position = round(new_position[0]), round(new_position[1])
