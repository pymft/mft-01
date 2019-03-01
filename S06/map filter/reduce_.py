import functools
lst = [1, 2, 3, 4, 5]
[fun(1), fun(2), fun(3), fun(4), fun(5)]   # map



def fun(a, b):
    return a * b

lst = [1, 2, 3, 4, 5]
[fun(1, 2), 3, 4, 5]
[fun(fun(1, 2), 3), 4, 5]
[fun(fun(fun(1, 2), 3), 4), 5]
fun(fun(fun(fun(1, 2), 3), 4), 5)

lst = [1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[(1!*2), 3, 4, 5]
[(2!*3), 4, 5]


lst = [1    , 2    , 3    , 5    ]
[2*3*5, 1*3*5, 1*2*5, 1*2*3]
# [lst.copy().remove(i) for i in lst]

[1*2*3*5/1, 1*2*3*5/2, 1*2*3*5/3, 1*2*3*5/5]

[mul/i for i in lst]







res = functools.reduce(fun, lst)
print(res)