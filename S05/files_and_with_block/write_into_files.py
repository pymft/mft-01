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
lines = []
for i in range(1, m+1):
    line = []
    for j in range(1, n+1):
        line.append(str(i * j))

    line_str = '\t'.join(line)
    lines.append(line_str)

text = '\n'.join(lines)
f.write(text)






f.close()