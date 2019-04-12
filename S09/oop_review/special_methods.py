class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x_new = self.x + other.x
        y_new = self.y + other.y
        return  Vector(x_new, y_new)


    def __neg__(self):
        return Vector(-self.x, -self.y)
    # __mul__, __div__, __sub__, __pow__ **,
    # __gt__ >, __ge__ >=,
    # __eq__ ==
    #


v1 = Vector(10, 6)
v2 = Vector(2, 3)

v1 and v2 # v1.__and__(v2)
v3 = v1 + v2
print(type(v3))
print(v3.x, v3.y)


v4 = -v1
print(type(v4))
print(v4.x, v4.y)
