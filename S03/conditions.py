# conditional statement
num1 = int(input('enter num1 : '))
num2 = int(input('enter num2 : '))
action = input("say something : ")

val = num1 + num2
cond = num1 > num2

if action == 'add':
    print(num1 + num2)

if action == 'sub':
    print(num1 - num2)

if action == 'mul':
    print(num1 * num2)

if action == 'div':
    print(num1 / num2)
