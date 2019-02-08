#       a=0          b=10        c=20            d=100
#       |            |           |               |
#       v            v           v               v
#  <----+############+-----------+###############+------>

a = 0
b = 10
c = 20
d = 100

# num = int(input("num = "))

# if (num > a and num < b) or (num > c and num < d):
#     print("is in the range!")
# else:
#     print("is not in the range!")

num = 5
if (num > a and num < d):
    if not (num > b and num < c):
        print("is in the range!")
    else:
        print("the number is the range of b to c ")
else:
    print("is not in the range!")
