import os
os.chdir(r"C:\Users\RASHMI\PycharmProjects\pythonWorkspace\Files")

# 1.. count number of characters in line**************************************
# with open("example1.txt") as file:
#     ch_count = 0
#     for line in file:
#         ch_count += len(line)
# print(ch_count)

# 2.. count number  of character in file without using len +++++++++++++++++++++++++++++++++++++++++++++
# with open("example1.txt") as file:
#     count_l = 0
#     for line in file:
#         count_l += 1
# print(count_l)

# 3.. count number of words present in file
# with open("example1.txt") as file:
#     w_count = 0
#     for lines in file:
#         words = lines.split()
#         w_count += len(words)
#
# print(w_count)

# 4.. count number of words without using len function
# with open("example1.txt") as file:
#     w_count = 0
#     for lines in file:
#         words = lines.split()
#         for word in words:
#             w_count += 1
#
# print(w_count)

# 5.. print lines which are starting with vowels
# with open("example1.txt") as file:
#     for lines in file:
#         if lines.strip():
#             if lines[0] in "aeiouAEIOU":
#                 print(lines)

# 6.. print number of words in each line along with its line number?
# method1
# with open("example1.txt") as file:
#     line_no = 0
#     for lines in file:
#         if lines.strip():
#             line_no += 1
#             words = lines.split()
#             print(line_no, len(words))

# method-2 --- using enumerator
# with open("example1.txt") as file:
#     for index, item in enumerate(file, start=1):
#         print(index, len(item.split()))

# 7.. read lines in file from last line or reverse order?
# method -1
# with open("example1.txt") as file:
#     line_ = list(file)
#     for line in line_[::-1]:
#         print(line)

# method -2 using reversed
# with open("example1.txt") as file:
#     for line in reversed(list(file)):
#         print(line)

# 8.. count number of lines w/o loading the files into memory
# with open("example1.txt") as file:
#     line_no = 0
#     for lines in file:
#         line_no += 1
#
# print(line_no)

# 9.. count the number of spaces present in line
# method1 --- using builtin functions
# with open("example1.txt") as file:
#     count_s = 0
#     for line in file:
#         count_s += line.count(" ")
# print(count_s)

# method2 --- without builtin fun
# with open("example1.txt") as file:
#     count_s = 0
#     for line in file:
#         if line.strip():
#             for char in line:
#                 if char == " ":
#                     count_s += 1
#
# print(count_s)

# 10.. create dictionary with each word and its count pair in the file +++++++++++++=======
# with open("example1.txt") as file:
#     d = {}
#     for lines in file:
#         if lines.strip():
#             word = lines.split()
#             for words in word:
#                 if words not in d:
#                     d[words] = 1
#                 else:
#                     d[words] += 1
#
# print(d)

# 11.. print most occuring word in file ++++++++++++++++++++++++++++++++++++++++++++++++++++
# with open("example1.txt") as file:
#     d = {}
#     for line in file:
#         if line.strip():
#             word = line.split()
#             for words in word:
#                 if words not in d:
#                     d[words] = 1
#                 else:
#                     d[words] += 1
# print(d)
# least, *a, most = sorted(d.items(), key=lambda item: item[-1])
# print(most)

# 12.. print nth line from a file?
