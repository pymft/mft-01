def my_generator():
    yield 1
    yield 2
    yield 3


gen1 = my_generator()
gen2 = my_generator()


print(next(gen1))
print(next(gen1))
print(next(gen2))





# for i in gen:
#     print(i)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))