f = open("input.txt", mode='r')

line = f.readline()
print(line)

# print("hello")
# print("salam\n")
# print("salut")

#  EOF
while line != '':
    line = f.readline()
    print(line)

f.close()