class RememberStuff:
    instances = []

    def __init__(self, word):
        self.word = word
        # self.instances = self.instances + [self]
        if word in [s.word for s in self.instances]:
            print(f"{word} is duplicated")
        self.instances.append(self)

    def number_of_instances(self):
        return len(self.instances)

w1 = RememberStuff("Hello")
print(RememberStuff.instances)

w2 = RememberStuff("Hello")
print(RememberStuff.instances)

RememberStuff("Whatever")
print(RememberStuff.instances)
print(w2.number_of_instances())