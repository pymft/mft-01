import random

a = 1
b = 2**10

while True:
    # num = random.randint(a, b)
    num = int((a+b)/2)
    ans = input(f"is it {num}? (+, -, y)")

    if ans == '-':
        b = num
    elif ans == '+':
        a = num
    else:
        print(f"it's {num}")
        break
