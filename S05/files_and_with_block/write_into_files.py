f1 = open('input.txt')
text = f1.read()
lines = text.split('\n')  # ['  30  ', '50']
m_str = lines[0].strip()
n_str = lines[1].strip()
m = int(m_str)
n = int(n_str)

# n = int(lines[0].strip())
f1.close()

f = open('./output.txt', 'w')
for i in range(m, n+1):
    line = "*" * (i)
    line = line + '\n'
    f.write(line)

f.close()