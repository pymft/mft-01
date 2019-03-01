def calc(a, *numbers, method='+'):
    if method == '+':
        return sum(numbers)
    elif method == '*':
        res = 1
        for a in numbers:
            res *= a
        return res


def test(a, b, *args, mode=None):
    print(a, b, args, mode)


test(10, 20, 30, 40, 50, 60, 70, mode="a")


# res = calc(11, 22, 31, 4, 5, 6)
# print(res)