num = 1
# functions are callable
# print()
# type()
# id()
# tuple()

lst1 = [1, 2, 3]
print(id(lst1))

# lst1 = lst1 + [4]
lst1.append(4)
print(id(lst1))

text = "12313"

result = text.isdigit()
print(result)
