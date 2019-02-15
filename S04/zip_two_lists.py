lst_one = [10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, ]
lst_two = [-1, -2, -3, -4, -1, -2, -3, -4, -1, -2, -3, -4, -1, -2, -3, -4, -1, -2, -3, -4, -1, -2, -3, -4, -1, -2, -3, -4, ]

members = len(lst_one)

lst_zip = []
for i in range(members):
    a = lst_one[i]
    b = lst_two[i]
    val = (a, b)
    lst_zip.append(val)

print(lst_zip)
# lst_zip = [(10, -1), (20, -2), (30, -3), (40, -4)]

# if len(lst_one) == len(lst_two)
# for i in range(len(lst_one)):
#     a = lst_one[i]
#     b = lst_two[i]
#     diff = a - b
#     print(i, diff)


for a, b in lst_zip:
    print(a-b)

for a, b in zip(lst_one, lst_two):
    print(a-b)
