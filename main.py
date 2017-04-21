import sys

import sdl2
import sdl2.ext

from common import *
from wall import *
import game_systems


def main():
    num_of_players = 2
    sdl2.ext.init()
    window = sdl2.ext.Window(
        "Codebomber", (15 * Wall.sizex, 13 * Wall.sizey))
    window.show()

    world = sdl2.ext.World()
    render_system = game_systems.RenderSystem(window)

    # Adding systems to world
    world.add_system(render_system)

    sprite_factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

    step = 0  # used for generate_step
    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            elif event.type == sdl2.SDL_KEYUP:
                # ESC pressed - quit
                if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                    running = False
                    break
                # S pressed - generate step
                if event.key.keysym.sym == sdl2.SDLK_s:
                    generate_step(world, window, sprite_factory, num_of_players, step)
                    if step != 2:
                        step += 1
                    else:
                        step = 0
                # N pressed - generate new map
                if event.key.keysym.sym == sdl2.SDLK_n:
                    generate_map(world, window, sprite_factory, num_of_players)

        world.process()

    sdl2.ext.quit()
    return 0

if __name__ == "__main__":
    sys.exit(main())
