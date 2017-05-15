import threading


class PeriodicTimer(object):
    def __init__(self, interval, function, args):
        self.interval = interval
        self.function = function
        self.args = args
        self._timer = None

    def start(self):
        self._timer = threading.Timer(self.interval, self._execute, (self.args,))
        self._timer.start()

    def stop(self):
        self._timer.cancel()
        self._timer = None

    def _execute(self, args):
        self.function(*args)
        self._timer = threading.Timer(self.interval, self._execute, (args,))
        self._timer.start()
