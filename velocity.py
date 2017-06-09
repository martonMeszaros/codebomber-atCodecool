class Velocity(object):
    def __init__(self):
        self.x = 0
        self.y = 0

    def get_velocity(self):
        return (self.x, self.y)

    def set_velocity(self, new_velocity):
        self.x = new_velocity[0]
        self.y = new_velocity[1]
