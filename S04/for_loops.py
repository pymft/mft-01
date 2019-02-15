
lst = [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]

for a, b in lst:
    print(a, b)

for val in lst:
    a, b = val 
    print(a, b)

for i in range(len(lst)):
    val = lst[i]
    a, b = val
    print(a, b)