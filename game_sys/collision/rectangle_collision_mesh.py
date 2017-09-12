
class RectangleMesh:
    def __init__(self, x=0, y=0, w=0, h=0):
        self._top = y
        self._bottom = y + h
        self._left = x
        self._right = x + w
        self.transform = 0, 0

    def top(self):
        return self._top + self.transform[1]

    def bottom(self):
        return self._bottom + self.transform[1]

    def left(self):
        return self._left + self.transform[0]

    def right(self):
        return self._right + self.transform[0]
