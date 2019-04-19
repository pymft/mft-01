class Bird:
    def __init__(self, type_of_bird='bird'):
        self.type_of_bird = type_of_bird
        self.alive = True

    def fly(self):
        print(f"{self.type_of_bird} is flying")

    def is_alive(self):
        if self.alive:
            print("this bird is alive")
        else:
            print("this bird is no more. it ceased to be.")


class Parrot(Bird):
    def __init__(self):
        super().__init__(type_of_bird='Parrot')


class Penguin(Bird):
    def __init__(self):
        super().__init__(type_of_bird='Penguin')

    def fly(self):
        print("Penguins cannot fly dude!")


pingo = Penguin()
pingo.fly()

p = Parrot()
p.fly()
p.alive = False
p.is_alive()

crow = Bird()
crow.fly()
crow.is_alive()