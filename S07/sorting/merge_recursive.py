# https://www.aparat.com/v/1l3DB/%D9%86%D9%85%D8%A7%DB%8C%D8%B4_%D8%B7%D8%B1%D8%B2_%DA%A9%D8%A7%D8%B1_15_%D8%A7%D9%84%DA%AF%D9%88%D8%B1%DB%8C%D8%AA%D9%85_%D9%85%D8%B1%D8%AA%D8%A8_%D8%B3%D8%A7%D8%B2%DB%8C_%28Sorting%29_%D8%AF%D8%B1_6%D8%AF%D9%82%DB%8C%D9%82%D9%87

def merge(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    right = merge(lst[mid:])
    left = merge(lst[:mid])

    res = []

    while right and left:
        if right[0] < left[0]:
            tmp = right.pop(0)
        else:
            tmp = left.pop(0)

        res.append(tmp)

    res.extend(left)
    res.extend(right)

    return res


lst = [1, 100, 23, -1]
print(merge(lst))
