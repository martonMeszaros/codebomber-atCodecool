import sys
import time

import sdl2
import sdl2.ext

import game_sys
from common import Color
from player import Player
from wall import GenerateWalls, Wall
from bomb import Bomb
from custom_world import CustomWorld


def game_tick(data, time_diff):
    data.sprite.position = (data.sprite.position[0] + 20, data.sprite.position[1])


def main():
    config = game_sys.config
    # Set individual class sprite sizes based on Data.sprite_size
    Wall.size = config.sprite_size

    # Initialize sdl2, window, and world
    sdl2.ext.init()
    window = sdl2.ext.Window(
        "Codebomber", (config.map_size[0] * Wall.size[0], config.map_size[1] * Wall.size[1]))
    window.show()
    world = CustomWorld()

    # Initialize game systems and add them to world
    render_system = game_sys.RenderSystem(window)
    world.add_system(render_system)

    sprite_factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    test_bomb = Bomb(world, sprite_factory.from_color(Color.black, config.sprite_size), (0, 0), None)
    world.add_system(game_sys.BombMovementTest())

    # last_time = time.perf_counter()
    running = True
    while running:
        # current_time = time.perf_counter()
        # time_diff = current_time - last_time
        # last_time = current_time
        # game_tick(Bomb(world, sprite_factory.from_color(Color.black, config.sprite_size), (0, 0), None), time_diff)
        # Event handling
        events = sdl2.ext.get_events()
        for event in events:
            # QUIT
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            # KEYUP events
            elif event.type == sdl2.SDL_KEYUP:
                # ESC pressed - quit
                if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                    running = False
                    break
                # S pressed - generate step
                if event.key.keysym.sym == sdl2.SDLK_s:
                    GenerateWalls.generate_step(world, window, sprite_factory, config.number_of_players)
                # N pressed - generate new map
                if event.key.keysym.sym == sdl2.SDLK_n:
                    GenerateWalls.generate_map(world, window, sprite_factory, config.number_of_players)
                if event.key.keysym.sym == sdl2.SDLK_b:
                    test_bomb.velocity.set_velocity((0.5, 0))
                if event.key.keysym.sym == sdl2.SDLK_v:
                    test_bomb.velocity.set_velocity((0, 0))
                if event.key.keysym.sym == sdl2.SDLK_c:
                    test_bomb.bombdata.position = 0, 0
                    test_bomb.sprite.position = 0, 0

        world.process()

    sdl2.ext.quit()
    return 0

if __name__ == "__main__":
    sys.exit(main())
