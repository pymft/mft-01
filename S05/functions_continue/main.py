def my_fun(a, b, c, d=100, e=20):

    print(a, b, c, d, e)
    return


def my_sum(*args):
    return sum(args)


def my_range(*args):
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        # start, stop, step = args[0], args[1], args[2]
        start, stop, step = args
    else:
        print("Invalid!")
    print (start, stop, step)


my_range(10, 100, 2)