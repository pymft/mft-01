def fun1(n):
    return n ** 2

fun2 = lambda n: n ** 2


num = 10
print(fun1(num))
print(fun2(num))


lst = [1, 2, 3, 4, 5, 6, 7]
out = map(lambda x: x**2+10, lst)
print(list(out))

fil = filter(lambda x: x % 2, lst)
print(list(fil))