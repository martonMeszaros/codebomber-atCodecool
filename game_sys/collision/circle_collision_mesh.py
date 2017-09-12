
class CircleMesh:
    def __init__(self, x=0, y=0, r=0):
        self._x = x
        self._y = y
        self.r = r
        self.transform = 0, 0

    def x(self):
        return self._x + self.transform[0]

    def y(self):
        return self._y + self.transform[1]
