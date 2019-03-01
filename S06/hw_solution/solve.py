import etefagh


def describe(t, t1, t2):
    if t < t1:
        return 'S'
    elif t > t2:
        return 'L'
    else:
        return 'M'


data = etefagh.data

diff = []
tags = []

starts = data[:-1]
stops = data[1:]

for i, e in zip(starts, stops):
    t = e-i
    tag = describe(t, 300, 400)
    diff.append(t)
    tags.append(tag)


tags_str = ''.join(tags)

pat = "MSSSSM"
start_etefagh = tags_str.find(pat)

if not start_etefagh == -1:
    stop_etefagh = start_etefagh + len(pat)

    start_time, stop_time = data[start_etefagh+1], data[stop_etefagh-1]
    val = stop_time - start_time
    print(val, start_time, stop_time)
    print(tags_str)
