lst = [(1, 10), (23, 0), (1, 5), (234, 2), (12, 312)]

print(lst, "before sorted")
# lst.sort()
f = lambda x: x[1]
new_list = sorted(lst, key=f)
print(lst, "after sorted")
print(new_list, "new_list")
lst.sort(key=f)
print(lst, "after calling sort method of the instance")

