class Rectangle:
    shape = "mostatil"
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # self.area = width * height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2


r1 = Rectangle(10, 5)
r1.height =7
# print(r1.area)
print(r1.get_area())
print(r1.get_perimeter())


print(Rectangle.__dict__)
print(r1.__dict__)