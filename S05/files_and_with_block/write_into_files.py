f1 = open('input.txt')
text = f1.read()
n = int(text)
print(n)
f1.close()

f = open('./output.txt', 'w')
for i in range(1, n+1):
    line = "*" * (i)
    line = line + '\n'
    f.write(line)

f.close()