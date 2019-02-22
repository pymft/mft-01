import math


def length_of_vector(x, y):
    answ_2 = math.pow(x, 2) + math.pow(y, 2)
    res = math.sqrt(answ_2)
    return res


val = length_of_vector(4, 3)
print(val)