m = 10
pat = "*"
pat_ws = '-'

for i in range(m):
    raw = pat*(2*i + 1)

    line = f"{raw:-^21}"
    print(line)