class Rectangle:
    shape = "mostatil"
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # self.area = width * height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return (self.width + self.height) * 2


r1 = Rectangle(10, 5)
r1.height = 7
print(r1.area, r1.perimeter)
r1.width = 2
print(r1.area, r1.perimeter)
r1.height = 1
print(r1.area, r1.perimeter)

#
# # print(r1.get_area())
# # print(r1.get_perimeter())
#
#
# print(Rectangle.__dict__)
# print(r1.__dict__)