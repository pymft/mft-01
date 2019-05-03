a = 10
b = 0
lst = [1, 2, 3, 4]
try:
    print(lst[10])
    value = a / b
    print(value)
except ZeroDivisionError as e:
    print(e)
    print("ZeroDivisionError")
except IndexError as e:
    print(e)
    print(f"IndexError ; {e.args[0] }")
finally:
    print("Finally")

print("I'm here ")


