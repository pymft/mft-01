from time import time
import urllib.request


class Browser:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if args[0] in cls._instances.keys():
            return Browser._instances[args[0]]
        return super().__new__(cls)

    def __init__(self, url):
        self.url = url
        self.__data = None
        Browser._instances.update({self.url: self})

    @property
    def data(self):
        if not self.__data:
            with urllib.request.urlopen(self.url) as req:
                self.__data = req.read().decode('utf8')

        return self.__data

    def links(self):
        pass


b = Browser("https://python.org")
c = Browser("https://python.org")


b.links[5].data

# print(id(b))
# print(id(c))
#
# times = []
# times.append(time())
# text = b.data
# times.append(time())
# print(times[-1] - times[-2])
# print(len(text))
#
# times.append(time())
# text = c.data
# times.append(time())
# print(times[-1] - times[-2])
# print(len(text))