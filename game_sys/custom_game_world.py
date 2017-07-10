import time

import sdl2.ext


class CustomGameWorld(sdl2.ext.World):
    def __init__(self):
        super(CustomGameWorld, self).__init__()
        self._last_time = None

    def process(self):
        if self._last_time:
            now_time = time.perf_counter()
            self.delta_time = now_time - self._last_time
            self._last_time = now_time
        else:
            self._last_time = time.perf_counter()
            self.delta_time = 0.0
        super(CustomGameWorld, self).process()
