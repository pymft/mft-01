def is_even(n):
    return n % 2 == 0


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = [n for n in lst if is_even(n)]

for i in filter(is_even, lst):
    print(i)
print(evens)

