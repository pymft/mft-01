table = "Employee; DELETE TABLE "

f"select * from {table}"


class Employee:

    def __init__(self, name):
        self.name = name

Employee("John")