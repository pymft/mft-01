import re
from time import time
import urllib.request

class MySpecialError(TypeError):
    pass


class Browser:
    _instances = {}

    def __init__(self, url):
        if not isinstance(url, str):
            raise MySpecialError
        if url in self._instances:
            raise ValueError

        self.__url = url
        self.__data = None
        Browser._instances.update({self.__url: self})


urls = ["https://python.org", "https://python.org", "www.google.com", 12323423423]
for url in urls:
    try:
        print(url)
        Browser(url)
    except BaseException as e:
        print(f"you cannot open url {url} ")
    # except TypeError as e:
    #     print(f"invalid type for url field")



