class Color:
    colors_map = {'red': 31, 'green':32, 'yellow':33, 'blue':34}

    def __init__(self, c):
        self.c = self.colors_map[c]

    def __call__(self, f):
        def inner(*args, **kwargs):
            result = f(*args, **kwargs)
            return f"\033[{self.c};1m{result}\033[0m"
        return inner


@Color('blue')
def echo(text):
    return text

print(echo("hello"))
