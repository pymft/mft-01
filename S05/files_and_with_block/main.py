# abs path
# f = open(r"C:\Users\Student\PycharmProjects\codes\S05\files_and_with_block\input.txt")
#
# C:\Users\Student\PycharmProjects\codes\S05\formatting_strings\readme.md
# C:\Users\Student\PycharmProjects\codes\S05\files_and_with_block
#
# ..\formatting_strings\readme.md
#
# f = open('../formatting_strings/readme.md')
# .   current directory
# ..  parent directory
# read from file


f1 = open('input.txt')
text = f1.read(10)
print(text)
text = f1.read(10)
print(text)
f1.close()


#
# # write
# f2 = open('output.txt', mode='w')
# f2.close()
#
#
# # write , check if exists
# f3 = open('output_2.txt', mode='x')
