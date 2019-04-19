class Bird:
    def __init__(self, name):
        self.name = name
        self._masalan_protected = "hello"
        self.__hidden = "Something"

    def show_private_var(self):
        print(self.__hidden)



p = Bird("Parrot")
print(p.name)
p.show_private_var()
print(p._Bird__hidden)