# 1. create two lists into dictionary as value pair ******************************
# l1 = ["Hello", "world"]
# l2 = [50, 100]
# d = {}
# for item1, item2 in zip(l1, l2):
#     d[item1] = item2
# print(d)



# 2.a print city and its temperature seperately *************************************
# temperature = {"Bangalore": (26, 32), "chennai": (29, 35), "Delhi": (31, 36)}

########### method1 ##############
# l = []
# for key, val in temperature.items():
#     item = (key, val)
#     l.append(item)
# print(l)

########## method2 #############
# print(list(temperature.items()))

########## method2 #############
# for key, val in temperature.items():
#     l.append((key, val))
# print(l)

# 2.b print the city, min temp, max temp seperately from the given dictionary
# temperature = {"Bangalore": (26, 32), "chennai": (29, 35), "Delhi": (31, 36)}
# l = []
# for key, (val1, val2) in temperature.items():
#     l.append((key, (val1, val2)))
# print(l)

# 3 create list of tuples with the index and value of each character
# s = "hello"
# l = []
# for index, val in enumerate(s):
#     l.append((index, val))
# print(l)

# 4 WAP remove duplicate from the string
# s = "hello hai"
# res = ""
# for i in s:
#     if i not in res:
#         res = res + i
# print(res)



