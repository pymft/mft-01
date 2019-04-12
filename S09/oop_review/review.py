class Rectangle:
    name = "Rectangle"

    def __init__(self, w, h):
        self.width = w
        self.height = h

    @property
    def area(self):
        return self.width * self.height

    @area.setter
    def area(self, value):
        ratio_area = value / self.area
        ratio = ratio_area ** 0.5
        self.width *= ratio
        self.height *= ratio

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    @perimeter.setter
    def perimeter(self, value):
        ratio = value / self.perimeter
        self.width *= ratio
        self.height *= ratio



r1 = Rectangle(10, 2)
# r1.width = 10
# r1.height = 2
print(r1.width, r1.height,  r1.area, r1.perimeter)

r1.area = 80
print(r1.width, r1.height,  r1.area, r1.perimeter)

r1.perimeter = 24
print(r1.width, r1.height,  r1.area, r1.perimeter)

# r2 = Rectangle(10, 3)
# # r2.width = 10
# # r2.height = 3
# print(r2.width, r2.height,  r2.area)