import random
secret = random.randint(1, 16)

while True:
    num = int(input("guess the number: "))
    if num > secret:
        print("your number is greater than secret")
    elif num < secret:
        print("your number is lesser than secret")
    else:
        print("BINGO!")
        break