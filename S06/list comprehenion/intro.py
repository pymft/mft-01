range(1, 8)  # [1, 2, 3, 4, 5, 6, 7]

def f(n):
    return n ** 2 + 1


lst = [1, 2, 3, 4, 5, 6, 7]
# [f(1), f(2), f(3), f(4), f(5), f(6), f(7)]
# [2, 5, 10, 17, ...]
#
# out = []
# for value in lst:
#     res = f(value)
#     out.append(res)
#
# print(out)

out = [f(value) for value in lst]

map_out = map(f, lst)

print(map_out)
print(list(map_out))

for i in map(f, lst):
    print(i)

for i in [f(value) for value in lst]:
    print(i)

print([i ** 2+1 for i in range(10)])

