import sdl2.ext

from bomb.bomb import BombData
from bomb.explosion import ExplosionData, Explosion


class BombTimer(sdl2.ext.Applicator):
    def __init__(self, sprite_factory):
        super(BombTimer, self).__init__()
        self.componenttypes = BombData, sdl2.ext.Sprite
        self.sprite_factory = sprite_factory

    def process(self, world, componentsets):
        delta_time = world.delta_time
        for bomb_data, sprite in componentsets:
            bomb_data.timer -= delta_time
            if bomb_data.timer <= 0:
                bombs = world.get_entities(bomb_data)
                for bomb in bombs:
                    if bomb.sprite.position == sprite.position:
                        bomb_data.player.playerdata.bombs_placed -= 1
                        Explosion(world, self.sprite_factory, sprite.position, bomb_data.player.playerdata.power)
                        bomb.delete()
                        break


class ExplosionTimer(sdl2.ext.Applicator):
    def __init__(self):
        super(ExplosionTimer, self).__init__()
        self.componenttypes = ExplosionData, sdl2.ext.Sprite

    def process(self, world, componentsets):
        delta_time = world.delta_time
        for explosion_data, sprite in componentsets:
            explosion_data.fallout -= delta_time
            if explosion_data.fallout <= 0:
                explosions = world.get_entities(explosion_data)
                id_to_delete = id(sprite)
                for explosion in explosions:
                    if id(explosion.sprite) == id_to_delete:
                        explosion.delete()
                        break
