class Rectangle:
    def __init__(self, w, h):
        print("hello from rectangle")
        self.w = w
        self.h = h

    def area(self):
        return self.h * self.w


class Square(Rectangle):
    def __init__(self, a):
        print("hello from square")
        super().__init__(a, a)




# r = Rectangle(10, 2)
# print(r.area())

s = Square(2)
print(s.w, s.h)
print(s.area())