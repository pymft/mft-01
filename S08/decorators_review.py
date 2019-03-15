# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def main():
#     return "Hello"
#
#
# my_decorator = app.route('/login')
#
#
# @my_decorator
# def login():
#     return "<h1>login page</h1>"
#
# app.run()

def color(name):
    color_dict = {'green': '2', 'red': '1'}
    def decorator(f):
        def inner(*args, **kwargs):
            out = f(*args, **kwargs)
            out = "\033[3" + color_dict[name] + ';1m' + out + "\033[0m"
            return out
        return inner
    return decorator

@color('green')
def say_hello():
    return "hello"

@color('red')
def echo(s):
    return s


res1 = say_hello()
res2 = echo("hi")

print(res1)
print(res2)


