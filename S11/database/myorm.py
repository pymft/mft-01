class DB:
    def __init__(self, **kwargs):
        print(self.__class__.__name__)
        print(self.__class__.__dict__)
        print(kwargs)


class Employee(DB):
    name = None
    age = None

    # def __init__(self, name, age, salary, adress):
    #     self.name = name
    #     self.age = age
    #     self.salary = salary
    #     self.address = adress
    #
    #     columns = ', '.join(tuple(self.__dict__))
    #     values = str(tuple(self.__dict__.values()))
    #     query = f"INSERT INTO {self.__class__.__name__} ({columns}) VALUES {values}"
    #     print(query)
    #


class Track(DB):
    name = None
    milliseconds = None
    artist = None


# p = Employee('john', 32, 200000)

Employee(name='john', age=32)

print('--------------------------------------------------------')
Track(name='Highway to hell', milliseconds=1231, artist='whatever')
