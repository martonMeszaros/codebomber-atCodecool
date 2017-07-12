import sdl2.ext

from bomb.bomb import BombData


class BombTimer(sdl2.ext.Applicator):
    def __init__(self):
        super(BombTimer, self).__init__()
        self.componenttypes = BombData, sdl2.ext.Sprite

    def process(self, world, componentsets):
        delta_time = world.delta_time
        for bomb_data, sprite in componentsets:
            bomb_data.timer -= delta_time
            if bomb_data.timer <= 0:
                bombs = world.get_entities(bomb_data)
                for bomb in bombs:
                    if bomb.sprite.position == sprite.position:
                        position = sprite.position
                        bomb_data.player.playerdata.bombs_placed -= 1
                        bomb.delete()
                        # Trigger explosion
                        break
