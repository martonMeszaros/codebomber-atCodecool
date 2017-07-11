import sys

import sdl2
import sdl2.ext

import game_sys.game_config
import player.movement
from common import Color
from player.player import Player
from map_components.wall import Wall, __gen_permawalls, generate_map
from map_components.floor import Floor
from bomb.bomb import Bomb
from game_sys.custom_game_world import CustomGameWorld


def init(config):
    # Initialize sdl2, window, and world
    sdl2.ext.init()
    window = sdl2.ext.Window("Codebomber", config.window_size)
    renderer = sdl2.ext.Renderer(
        window,
        logical_size=(config.map_size[0] * config.sprite_size[0], config.map_size[1] * config.sprite_size[1]),
        flags=sdl2.SDL_RENDERER_SOFTWARE
        )
    window.show()
    world = CustomGameWorld()

    sprite_factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)

    # Initialize game systems and add them to world
    world.add_system(sdl2.ext.TextureSpriteRenderSystem(renderer))

    Floor(world, sprite_factory.from_color(Color.grass, (config.map_size[0] * config.sprite_size[0], config.map_size[1] * config.sprite_size[1])))
    __gen_permawalls(world, renderer, sprite_factory)

    return window, world, sprite_factory, renderer


def main():
    config = game_sys.game_config.config

    # Initialize sdl2, window, and world
    window, world, sprite_factory, renderer = init(config)

    world.add_system(player.movement.BombMovementTest())
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
                # N pressed - generate new map
                if event.key.keysym.sym == sdl2.SDLK_n:
                    generate_map(world, renderer, sprite_factory, config.number_of_players)
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
