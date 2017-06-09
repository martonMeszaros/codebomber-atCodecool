import time

import sdl2
import sdl2.ext


class CustomWorld(sdl2.ext.World):
    def __init__(self):
        super(CustomWorld, self).__init__()
        self.last_time = None

    def process(self):
        if self.last_time:
            now_time = time.perf_counter()
            self.delta_time = now_time - self.last_time
            self.last_time = now_time
        else:
            self.last_time = time.perf_counter()
            self.delta_time = 0.0
        super(CustomWorld, self).process()
