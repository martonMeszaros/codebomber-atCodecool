import sys
import time

import sdl2
import sdl2.ext

import game_sys.game_config
import game_sys.render_system
import player.movement
from common import Color
from player.player import Player
from map_components.wall import GenerateWalls, Wall
from bomb.bomb import Bomb
from game_sys.custom_game_world import CustomGameWorld


def main():
    config = game_config.config
    # Set individual class sprite sizes based on Data.sprite_size
    Wall.size = config.sprite_size

    # Initialize sdl2, window, and world
    sdl2.ext.init()
    window = sdl2.ext.Window(
        "Codebomber", (config.map_size[0] * Wall.size[0], config.map_size[1] * Wall.size[1]))
    window.show()
    world = CustomGameWorld()

    sprite_factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

    # Initialize game systems and add them to world
    world.add_system(movement.BombMovementTest())

    renderer = render_system.RenderSystem(window)
    world.add_system(renderer)

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
