import os

os.chdir(r"C:\Users\RASHMI\PycharmProjects\pythonWorkspace\Files")

# 1.. count number of lines without loading file to a memory?
# with open("example1.txt") as file:
#     line_no = 0
#     for line in file:
#         line_no += 1
#     print(line_no)

# 2.. count number of commented line in file?
# with open("example1.txt") as file:
#     comm = 0
#     for line in file:
#         if line[0] == "#":
#             comm += 1
#     print(comm)

# 3.. print only even number line in a file
# with open("example1.txt") as file:
#     lnum = 0
#     for line in file:
#         if line.strip():
#             lnum += 1
#             if lnum % 2 == 0:
#                 print(line)

# 4.. count number of occurence of vowels in a file?
# with open("example1.txt") as file:
#     vowels = 0
#     for line in file:
#         for char in line:
#             if char in "aeiouAEIOU":
#                 vowels += 1
#     print(vowels)

# 5.. line number of lines not starting with vowels?
# with open("example1.txt") as file:
#     notvoewls = 0
#     for line in file:
#         if line[0] not in "aeiouAEIOU":
#             notvoewls += 1
#     print(notvoewls)

d = {"bang": 1, "mysore": 2}
print(d.get('my'))

