class Vector:
    def __init__(self, *args):
        print(args)
        self.dims = args

    @property
    def length(self):
        pow_two = map(lambda x: x**2, self.dims)
        sum_pow_two = sum(pow_two)
        return sum_pow_two ** 0.5

    def __add__(self, other):
        x_new = self.x + other.x
        y_new = self.y + other.y
        return Vector(x_new, y_new)

v1 = Vector(10, 6, 100, 20)
v2 = Vector(3, 50)
print(v1.length)
print(v2.length)
