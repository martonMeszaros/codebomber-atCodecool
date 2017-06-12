import sys
import time

import sdl2
import sdl2.ext

import game_sys
import movement
from common import Color
from player import Player
from wall import GenerateWalls, Wall
from bomb import Bomb
from custom_world import CustomWorld


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

    sprite_factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

    # Initialize game systems and add them to world
    world.add_system(movement.BombMovementTest())

    render_system = game_sys.RenderSystem(window)
    world.add_system(render_system)

    test_bomb = Bomb(world, sprite_factory.from_color(Color.black, config.sprite_size), (0, 0), None)
    running = True
    while running:
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
                # B pressed start moving test bomb
                if event.key.keysym.sym == sdl2.SDLK_b:
                    test_bomb.movement.velocity = 0.5, 0
                # V pressed stop moving test bomb
                if event.key.keysym.sym == sdl2.SDLK_v:
                    test_bomb.movement.velocity = 0, 0
                # C pressed reset test bomb position
                if event.key.keysym.sym == sdl2.SDLK_c:
                    test_bomb.movement.position = 0.0, 0.0
                    test_bomb.sprite.position = 0, 0

        world.process()

    sdl2.ext.quit()
    return 0

if __name__ == "__main__":
    sys.exit(main())
