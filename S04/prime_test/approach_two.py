num = 13

upper = int(num ** 0.5)
i = 2

while i <= upper and num % i > 0:
    i += 1     # i = i + 1

if (num - i) == 0:
    print("is prime")
else:
    print("is not prime")