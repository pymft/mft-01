class Test:
    name = "Something"


t1 = Test()
t1.name = "Something Else!"
t2 = Test()

Test.name = "New name of class"
print(t1.name)