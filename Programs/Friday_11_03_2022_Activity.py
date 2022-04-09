# 1.. count number of capitaal and small letter in as string and create a dictionary*****************

# s  = "NaMaStE"
# dd = defaultdict(int)
# for i in s:p
#     if "a" <= i <= "z":
#         dd[i] += 1
#     elif "A" <= i <= "Z":
#         dd[i] += 1
# print(dd)

# 2.. print extension of each file name in the list
file = ["youtube.txt", "yahoo.pdf", "microsoft.doc", "apple.xlsx"]
for i in file:
    fname, ext = i.split('.')
    print(ext)



# 3.. create a dictionary of character and its count without using inbuilt function ******************************
# method 1
# dd = defaultdict(int)
# char = "Hello"
# for i in char:
#     dd[i] += 1
# print(dd)

# method 2
# s = "hello"
# d = {}
#
# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)

# 4.. create dictionary with words and its count pair only if word is even length ################################
# s = "Hi Hi How are youu"
# words = s.split()
# d = {}
#
# for i in words:
#     if len(i) % 2 == 0:
#         d[i] = words.count(i)
# print(d)

# 5.. WAP sum all the numbers in the below string
# s = "sony12India567pvt2ltd"
# words = s.split()
# for i in words:



s = "hello"
for item1, item2 in enumerate(s):
    c = (item1, item2)
    print(c)