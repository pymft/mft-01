def is_palindrome(text):
    return text == text[::-1]


def my_max(lst):
    index = 0
    temp_max = lst[index]

    for i, val in enumerate(lst):
        if temp_max < val:
            temp_max = val
            index = i

    return temp_max







def combination(n, m):
    #