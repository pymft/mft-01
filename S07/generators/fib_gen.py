import math



def fib():
    a = 0
    yield a
    b = 1
    yield b
    while True:
        a, b = b, a+b
        yield int(math.log(b, 10))


gen = fib()


lst = []
for i in range(10000):
    tmp = next(gen)
    lst.append(tmp)

map_fun = lambda x: x[1] - x[0]
starts, stops = lst[:-1], lst[1:]
res = map(map_fun, zip(starts, stops))
print(list(res))
