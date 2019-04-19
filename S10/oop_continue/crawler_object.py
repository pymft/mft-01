from time import time
import urllib.request


class Browser:
    def __init__(self, url):
        self.url = url
        self.__data = None

    @property
    def data(self):
        if not self.__data:
            with urllib.request.urlopen(self.url) as req:
                self.__data = req.read().decode('utf8')

        return self.__data


b = Browser("https://python.org")
c = Browser("https://python.org")
times = []
times.append(time())
text = b.data
times.append(time())
print(times[-1] - times[-2])
print(len(text))
