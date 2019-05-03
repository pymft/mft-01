from collections import deque

d = deque([1, 2, 3, 4, 5], maxlen=5)

print(d)
d.append(100)
print(d)
d.rotate(2)
print(d)
