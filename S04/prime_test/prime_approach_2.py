# num = int(input('enter a number : '))
num = 2**30  - 1

is_prime = True

upper = int(num ** 0.5)

for i in range(2, num):
    if num % i == 0:        # check
        is_prime = False

if is_prime:
    print("the number is prime!")
else:
    print("it is not prime!")



