import os
os.chdir(r"C:\Users\RASHMI\PycharmProjects\pythonWorkspace\Files")

# 1.. WAP to get only the IP ipaddress and their count in log.txt file? *******************************
# with open("access-log.txt") as file:
#     d = {}
#     for lines in file:
#         if lines.strip():
#             words = lines.split()
#             if words[0] not in d:
#                 d[words[0]] = 1
#             else:
#                 d[words[0]] += 1
# print(d)

# 2.. print most occuring brand names from data.txt? *****************************************
# with open("data.txt") as file:
#     d = {}
#     for line in file:
#         if line.strip():
#             words = line.split('\t')
#             if words[0] not in d:
#                 d[words[0]] = 1
#             else:
#                 d[words[0]] += 1
# print(d)
# least, *a, most = sorted(d.items(), key=lambda item: item[-1])
# print(most)

# 3.. WAP to create a dictionary of message and its number of occurence in sample.log file? **********************

# with open("sample.log") as file:
#     d = {}
#     for line in file:
#         if line.strip():
#             words = line.split(" ")
#             if words[2] not in d:
#                 d[words[2]] = 1
#             else:
#                 d[words[2]] += 1
#
# print(d)


# 4.. print the countries based on their rank
# method1 --- without defaultdict
# with open("football.txt", encoding="UTF-8") as file: # ADD utf-8 whwnever u get unicode error
#     d = {}
#     for line in file:
#         if line.strip():
#             words = line.split('\t')
#             if words[1] not in d:
#                 d[words[1]] = 1
#             else:
#                 d[words[1]] += 1
#
# print(d)

#method2 --- using defaultdict
# from collections import defaultdict
# with open("football.txt", encoding="UTF-8") as file: # ADD utf-8 whwnever u get unicode error
#     d = defaultdict(int)
#     for line in file:
#         if line.strip():
#             words = line.split('\t')
#             if words[1] not in d:
#                 d[words[1]] += 1
#
# print(d)