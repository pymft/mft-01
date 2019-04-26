import re
from time import time
import urllib.request


class Browser:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if args[0] in cls._instances.keys():
            return Browser._instances[args[0]]
        return super().__new__(cls)

    def __init__(self, url):
        self.__url = url
        self.__data = None
        Browser._instances.update({self.__url: self})

    @staticmethod
    def __get_links(data):
        pat = "href=['\"]?(https?[^'\" >]+)"

        res = re.findall(pat, data)
        return res

    @property
    def data(self):
        if not self.__data:
            with urllib.request.urlopen(self.__url) as req:
                self.__data = req.read().decode('utf8')
        return self.__data

    @property
    def links(self):
        links_str = self.__get_links(self.data)
        return  [Browser(lnk) for lnk in links_str]
        # return map(Browser, links_str)

    def __repr__(self):
        return self.__url


b = Browser("https://python.org")

c = Browser("https://python.org")

