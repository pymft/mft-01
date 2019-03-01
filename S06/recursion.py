1, 1, 2, 3, 5, 8, 13, 21

def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)


def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


print(fact(100))
