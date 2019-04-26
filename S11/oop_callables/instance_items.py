class Sequence:
    instances = []

    def __init__(self, *args):
        self.args = args
        self.instances.append(self)

    def __getitem__(self, item):
        return self.instances[item]


s1 = Sequence(10, 20)
s2 = Sequence(10, 20)

s1[0]