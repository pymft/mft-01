class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


    def __add__(self, other):
        x_new = self.x + other.x
        y_new = self.y + other.y
        return Vector(x_new, y_new)

v1 = Vector(10, 6)
v2 = Vector(3, 50)
harchi = v1 + v2
print(harchi.x, harchi.y, harchi.length)
print(v1.length)