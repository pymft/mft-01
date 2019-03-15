class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # return None
        # print("hello, ", name)

    def say_your_name(self):
        print("Menya zaut ", self.name, ", mne ", self.age, " let")


# instantiate
hamid = Person("Hamid", 23)
p2 = Person("John", 100)
# print(p1.name)
# print(p2.name)
# p1.name = "John"
# p2.name = "Jack"

p2.say_your_name()

hamid.say_your_name()
# Person.say_your_name(hamid)

# text = "hello"
# text.upper()
# str.upper(text)