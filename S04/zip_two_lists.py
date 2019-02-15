lst_one = [10, 20, 30, 40]
lst_two = [-1, -2, -3, -4]


#
# Add code here !!! 
#

lst_zip = [(10, -1), (20, -2), (30, -3), (40, -4)]

# if len(lst_one) == len(lst_two)
# for i in range(len(lst_one)):
#     a = lst_one[i]
#     b = lst_two[i]
#     diff = a - b
#     print(i, diff)

for a, b in zip(lst_one, lst_two):
    print(a-b)
