import sdl2.ext

import game_sys.game_config


class Movement(object):
    def __init__(self, position):
        self.velocity = 0, 0
        self.position = position


class BombMovementTest(sdl2.ext.Applicator):
    def __init__(self):
        self.componenttypes = (Movement, sdl2.ext.Sprite)
        self.is_applicator = True
        self.config = game_sys.game_config.config

    def process(self, world, componentsets):
        delta_time = world.delta_time
        for movement, sprite in componentsets:
            old_position = movement.position
            new_position = (
                old_position[0] + (movement.velocity[0] * self.config.sprite_size[0] * delta_time),
                old_position[1] + (movement.velocity[1] * self.config.sprite_size[1] * delta_time)
            )
            movement.position = new_position
            sprite.position = round(new_position[0]), round(new_position[1])
