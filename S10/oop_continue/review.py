from math import sqrt


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2)


    def __repr__(self):
        return f"Vec({self.x}, {self.y})"



v = Vector(10, 20)
print(v)

v.x, v.y