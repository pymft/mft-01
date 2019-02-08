num = 6
pattern = "*"
pattern_whitespace = " "

# while
# *
# **
# ***
# ****
# *****
# ******
i = 0
while i < num:
    i += 1
    line = pattern * i
    print(line)


# while + str methods
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
i = 0
while i < num:
    i += 1
    line = "*" * (2*i-1)
    line_centered = line.center(2*num - 1)
    print(line_centered)

# if
#       *
#      * *
#     *   *
#    *     *
#   *       *
#  *         *

i = 0
while i < num:
    i += 1
    if i == 1:
        print(pattern.center(2*num - 1))
    else:
        line = " " * (2*i-3)
        line = "*" + line + "*"
        line_centered = line.center(2*num - 1)
        print(line_centered)









first_line = "*".center(2*num - 1)
print(first_line)
i = 1
while i < num:
    i += 1
    line = " " * (2*i-3)
    line = "*" + line + "*"
    line_centered = line.center(2*num - 1)
    print(line_centered)

# if
#       *
#      * *
#     *   *
#    *     *
#   *       *
#  ***********

i = 0
while i < num:
    i += 1
    if i == 1 or i == num:
        line = pattern * (2*i-1)
        print(line.center(2*num - 1))
    else:
        line = " " * (2*i-3)
        line = "*" + line + "*"
        line_centered = line.center(2*num - 1)
        print(line_centered)
