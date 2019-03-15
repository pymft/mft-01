def fib(n):
    yield 0
    yield 1
    a, b = 1, 1
    i = 1
    while i <= n:
        i += 1
        yield b
        a, b = b, a+b


obj = fib(5)
val = next(obj)
print(val)
val = next(obj)
print(val)
val = next(obj)
print(val)
val = next(obj)
print(val)
val = next(obj)
print(val)
val = next(obj)
print(val)
val = next(obj)
print(val)
val = next(obj)
print(val)
