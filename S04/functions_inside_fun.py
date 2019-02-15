def fun1(f):
    print(locals())
    f(lst)


def fun2():
    print(locals())
    sum(lst)


lst = [1, 2, 3]

fun1(sum)
fun2()