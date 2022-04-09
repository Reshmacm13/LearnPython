# def last_seq(l):
#     return l[-1]
#
# last_seq([1, 2, 3, "hai"])

# check multiply of two numbers
# mul = lambda a, b : a*b
# print(mul(10, 2))

# solve expression a**2+b**2+2*a*b
# exp = lambda a, b: a**2+b**2+2*a*b
# # print(exp(2,4))

# l = ["hai", "mam", "radar"]
# palin = lambda i: "palindrome" if i == i[::-1] else "not a palindrome"
# print(palin(l))

# cube and square of number using lambda exprwssion
# square_numbers = list(map(lambda x: x ** 2, numbers))
# print(square_numbers(5))

# convert to positive number
# l = [-5, -7, -6]
# conv  = lambda num: abs(num)
# print(list(map(conv, l)))

#              or
# print(list(map(abs, l)))

# WAP which are starting with ovwels
# l = ["Today", "is", "tuesday"]
# def vowels(l):
#     for word in l:
#         if word[0] in "aeiouAEIOU":
#             return word
# print(list(map(vowels, l)))

# square and cube of every number in given list
# l = [2, 3, 4, 5]
# sq = lambda num : [num ** 2, num ** 3]
# print(list(map(sq, l)))

# list of elements raise to the power of indesis **********************************
l = [2, 3, 4, 5]
l1 = []
# for item1, item2 in enumerate(l):
#     l1.append(item2 ** item1)
# print(l1)

# using function
# res  = []
# def power(num):
#     for item1, item2 in enumerate(num):
#         res = item2 ** item1
#         # l1.append(item2 ** item1)
#         print(res)
# power(l)

# ad the following list elements
# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 8]
# def sum(x, y):
#     return x + y
#
# print(list(map(sum, l1, l2)))

# print the list of length of each word
# s = "hi good afternoon"
# l = s.split()
# print(list(map(len, l)))

# WAP return all the words in uppercase
# s = "hi good Afternoon"
# l = s.split()
# print(list(map(str.upper, l)))

# WAP which returns all the strings starting with vowels in the given sentences
# s = "hi good afternoon"
# words = s.split()
# def sent(s):
#     for i in words:
#         if i[0] in "aeiouAEIOU":
#             return i
# print(list(filter(sent, s.split())))

# print odd number range of 1 to 50
# l = range(1, 51)
# def odd(n):
#     if n % 2 != 0:
#         return n
#
# print(list(filter(odd, l)))

# # return a list of string with odd length
# l  = ["hi", "how", "are", "you"]
# def odd(s):
#     if len(s) % 2 != 0:
#         return s

# print(list(filter(odd, l)))

# # return only +ve value from the list
# l = [10, 20, 12.5, -125, -5]
# def pos(num):
#     if num > 0:
#         return num
# print(list(filter(pos, l)))

# prime number print from 1 to 50 ******************************************
# l = list(range(1, 51))
# def prime(num):
#         if num > 1:
#             for i in range(2, num):
#                 if num % i == 0:
#                     break
#             else:
#                 return num
#
# print(list(filter(prime, l)))

