import sys

import sdl2
import sdl2.ext

from common import Color
import game_sys
from player import Player
from wall import GenerateWalls, Wall


def main():
    # Set player count based on the first argument passed
    if len(sys.argv) > 1:
        Player.count = int(sys.argv[1])

    # Initialize sdl2, window, and world
    sdl2.ext.init()
    window = sdl2.ext.Window(
        "Codebomber", (15 * Wall.size[0], 13 * Wall.size[1]))
    window.show()
    world = sdl2.ext.World()

    # Initialize game systems and add them to world
    render_system = game_sys.RenderSystem(window)
    world.add_system(render_system)

    sprite_factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

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
                    GenerateWalls.generate_step(world, window, sprite_factory, Player.count)
                # N pressed - generate new map
                if event.key.keysym.sym == sdl2.SDLK_n:
                    GenerateWalls.generate_map(world, window, sprite_factory, Player.count)

        world.process()

    sdl2.ext.quit()
    return 0

if __name__ == "__main__":
    sys.exit(main())
