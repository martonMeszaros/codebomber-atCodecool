import sys

import sdl2
import sdl2.ext

import game_sys.game_config
from game_sys.collision.collider import Collider
from game_sys.grid_coordinates import get_map_size
from game_sys.custom_game_world import CustomGameWorld
from game_sys.bomb_timer import BombTimer, ExplosionTimer
from game_sys.movement import PlayerMovement
from map_components.map_setup import gen_permawalls, generate_map
from map_components.floor import Floor
from player.player import Player
from common import Color


def init(config):
    # Initialize sdl2, window, and world
    sdl2.ext.init()
    window = sdl2.ext.Window("Codebomber", config.window_size)
    renderer = sdl2.ext.Renderer(
        window,
        logical_size=get_map_size(),
        flags=sdl2.SDL_RENDERER_SOFTWARE
        )
    window.show()
    world = CustomGameWorld()

    sprite_factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)

    # Initialize game systems and add them to world
    world.add_system(PlayerMovement())
    world.add_system(Collider())
    world.add_system(BombTimer(sprite_factory))
    world.add_system(ExplosionTimer())
    world.add_system(sdl2.ext.TextureSpriteRenderSystem(renderer))

    Floor(world, sprite_factory.from_color(Color.grass, get_map_size()))
    gen_permawalls(world, sprite_factory)
    generate_map(world, sprite_factory, config.number_of_players)
    players = list()
    for _ in range(config.number_of_players):
        players.append(Player(world, sprite_factory.from_image("assets/player.png")))

    return window, world, sprite_factory, renderer, players


def main():
    config = game_sys.game_config.config

    # Initialize sdl2, window, and world
    window, world, sprite_factory, renderer, players = init(config)

    running = True
    while running:
        # Event handling
        events = sdl2.ext.get_events()
        for event in events:
            # QUIT
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            # KEYDOWN events
            elif event.type == sdl2.SDL_KEYDOWN:
                key = event.key.keysym.sym
                for player in players:
                    if key in player.controls.movement:
                        player.movement_pressed(key)
            # KEYUP events
            elif event.type == sdl2.SDL_KEYUP:
                key = event.key.keysym.sym
                # ESC pressed - quit
                if key == sdl2.SDLK_ESCAPE:
                    running = False
                    break
                for player in players:
                    if key == player.controls.bomb_placement:
                        player.place_bomb(world, sprite_factory)
                    elif key in player.controls.movement:
                        player.movement_released(key)

        world.process()

    sdl2.ext.quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
