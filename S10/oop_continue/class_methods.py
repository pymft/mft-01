class A:
    def show(self, text):
        print(text)


class B:
    @staticmethod
    def show(text):
        print(text)

class C:
    @classmethod
    def show(cls, text):
        print(text)


a = A()
print(type(a.show))
print(type(A.show))
A.show(a, "hello")


b = B()
print(type(b.show))
print(type(B.show))

c = C()
print(type(c.show))
print(type(C.show))
