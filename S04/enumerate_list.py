lst = [1, 32, 12, 331, 90]

# enumerated_lst = [(0, 1), (1, 32), (2, 12), (3, 331), (4, 90)]
enumerated_lst = []
for i in range(len(lst)):
    val = (i, lst[i])
    enumerated_lst.append(val)

print(enumerated_lst)

for i, val in enumerate(lst):
    print(i, val)