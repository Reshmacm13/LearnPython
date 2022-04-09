# ********** Traversing through for loop **************
# String
# s = "Hello World"
# for ele in s:
# print(ele)

# list
# l = [10, 20, 30, 40, 50]
# for li in l:
#     print(li)

# tuple
# t = (1, 2, 3, 4, 5)
# for t1 in t:
#     print(t1)

# set
# s = {1, 13, 11, 30, 4}
# for s1 in s:
#     print(s1)

# Dictionaries
# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# for item in d:
#     print(item, end='')

# ******************************** print 1 to 10 *******************
# for num in range(1, 11):
#     print(num)

# ******************************** print 10 to 0 *******************
# for num in range(10, 0, -1):
#     print(num)

# ******************************** print even numbers *******************
# for num in range(1, 51, 1):
#     if num % 2 == 0:
#         print(num)

# ******************************** print index and items in given iterables *************
# s = 'Namaste'
# for i in range(len(s)):
#     print(i, s[i])

# ****************************** convert lowercase to uppercase and viceversa ***************
# a = 'NaMaStE'
# res = ''
# for char in a:
#     if 'a' <= char <= 'z':
#         res = res + chr(ord(char) -32)
#     elif 'A' <= char <= 'Z':
#         res = res + chr(ord(char) +32)
#     else:
#         res += char
# print(res)

# ******************************  count number of index present in iterables ****************
# n = [1, 2, 3, 4, 5]
# count = 0
# for ele in n:
#     count = count +1
# print(count)

# ******************************  Number of words present *****************
# words = "Hai Hello Namaste"
# s = words.split()
# count = 0
# for word in s:
#     count += 1
# print(count)

# ****************************** print repeated char in string *************
# s = "MADAM"
# rep = ''
# for c in s:
#     if s.count(c) > 1:
#         if c not in rep:
#             rep = rep + c
# print(rep)

# ****************************** print duplicate char w/o inbuilt function **************
# s = "NAMASTE"
# duplicate = ''
# not_duplicate = ''
# for c in s:
#     if c not in not_duplicate:
#         not_duplicate = not_duplicate + c
#     else:
#         duplicate = duplicate + c
#
# print(set(duplicate))
# print("".join(not_duplicate))

# ****************************** Index of specified character ***********************
# c = 'python'
# search = 'y'
# for i in range(len(c)):
#     if c[i] == search:
#         print(i)

# *************************** first occurence in given string **************
# c = 'NaAMASTE'
# search = 'A'
# for i in range(len(c)):
#     if c[i] == search:
#         print(i)
#         break

# ************************ second occurence ***********************
# c = 'NAMASTE'
# search = 'A'
# count = 0
# for i in range(len(c)):
#     if c[i] == search:
#         count += 1
#         if count == 2:
#             print(i)

# ************************ print all words starting with ovewls ************
# words = "Hai how are you"
# s = words.split()
# for word in s:
#     if word[0] in "aeiouAEIOU":
#         print(word)

# ************************ print all words ending with ovewls ************
# words = "Hai how are you"
# s = words.split()
# for word in s:
#     if word[-1] in "aeiouAEIOU":
#         print(word)

# ************************ create list of words having even length *************
# words = "hai good afternoon test"
# s = words.split()
# l = []
# for word in s:
#     if len(word) % 2 == 0:
#         l.append(word)
# print(l)

# *********************** create list of tuples with word and length ************
# words = "hai good afternoon test"
# s = words.split()
# l = []
# for word in s:
#     item = word, len(word)
#     l.append(item)
# print(l)

# *********************** create dictionaries word and its length pair only word starting with vowels **********
# words = "hai good afternoon test"
# s = words.split()
# d = {}
# for word in s:
#     if word[0] in "aeiouAEIOU":
#         d[word] = len(word)
# print(d)

# ************************ create dirct with letter and word starting with letter pair in sentence *******
# words = "hai good afternoon test test123"
# s = words.split()
# d = {}
# for word in s:
#     if word[0] not in d:
#         d[word[0]] = [word]
#     else:
#         d[word[0]].append(word)
# print(d)

# ********************* create dirct with characetr and index pair ************
# s = 'hello world'
# d ={}
# for i in range(len(s)):
#     if s[i] not in d:
#         d[s[i]] = [i]
#     else:
#         d[s[i]].append(i)
# print(d)

# ************************* create dictionary with characters and its ASCII value in given string *****************
# c = "Namaste"
# d = {}
# for i in c:
#     d[i] = ord(i)
# print(d)

# ************************ create a directory with value of integer with dictionary **************
# d = {"a": 1, "b": "hello", "c": 85, "d": 12.5, "e": [1, 2, 3]}
# res = {}
# for i in d:
#     if isinstance(d[i], int):
#         res[i] = d[i]
# print(res)

# ************************ create dictionary if value is of string datatype reverse and store **********
# d = {"a": 1, "b": "hello", "c": 85, "d": 12.5, "e": [1, 2, 3]}
import itertools

res = {}
# for k, v in d.items():
#     if isinstance(v, str):
#         res[k] = v[::-1]
#     else:
#         res[k] = v
# print(res)

# # *********************** create dictionary with length and word pair **************************
# s = "hi how are you doing today test"
# d = {}
# words = s.split()
# for word in words:
#     d[word] = len(word)
# print(d)

# defaultdict

# ***********************  create dictionary with index and word pair *******************
# s = "hi how are you doing today test"
# d = {}
# words = s.split()
# for index, item in enumerate(words):
#     d[index] = item
# print(d)

# defaultdict

# ********************** create dictionary elements of l1 will be key and l2 will be the value *************
# l1 = ["hi", "hello"]
# l2 = [10, 50]
# d = {}
# for item1, item2 in zip(l1,l2):
#     d[item1] = item2
# print(d)

# ********************** create dictionary elements of l1 will be key and l2 will be the value *************

# **************** Error
# l1 = ["hi", "hello", "hel"]
# l2 = [10, 50]
# d = itertools
# for item1, item2 in itertools.zip_longest(l1, l2):
#     d[item1]: item2
# print(d)

