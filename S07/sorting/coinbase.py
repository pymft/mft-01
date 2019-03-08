from data import bitcoin

# # solution
# # 5-min periods
# res = sorted(bitcoin, key=lambda x: x[2]-x[1])
# print(res[-1])

f_fil = lambda x: (x[4] - x[3]) > 0
res = filter(f_fil, bitcoin)

f_sort = lambda x: x[2] - x[1]
val = sorted(res, key=f_sort)

top_ten = val[-10:]
volumes = map(lambda x: x[-1], top_ten)
print(sum(volumes))


