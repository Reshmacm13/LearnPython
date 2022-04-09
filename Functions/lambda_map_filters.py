# ******************** LAMBDA *****************************************************
# 1.. lambda expression to check even or not?

# evens = lambda n: n % 2 == 0
# print(evens(2))

# evens = lambda n: "even" if n % 2 == 0 else "odd"
# print(evens(7))

# 2.. lambda expression to check palindrome or not?
# palin = lambda s: "palindrome" if s == s[::-1] else "not palindrome"
# print(palin("mome"))

# 3.. lambda return last element of any sequence
# ele = lambda e: e[-1]
# print(ele('123'))

# 4.. lambda multiply of two numbers
# mul = lambda m,n: m *n
# print(mul(10, 2))

# 5.. print a ** 2 + b**2 +2*a*b
# f = lambda a, b: a ** 2 + b**2 +2*a*b
# print(f(2, 4))

# 6.. cube and square of given num
# c_s = lambda n: [ n**2, n**3]
# print(c_s(2))

# ************************************ MAPS ****************************************************************
# 1.. check palindrome or not in list
# palin = lambda s: "palindrome" if s == s[::-1] else "Not palindrome"
# l = ["MOM", "DAD", "SON"]
# print(list(map(palin, l)))

# 2.. check list even or odd?
# l = [2, 3, 4, 5, 6, 7, 8]
# num = lambda n: "even" if n % 2 == 0 else "odd"
# print(list(map(num, l)))

# 3.. convert -ve number to +ve number in given list
# l = [-5, 10, 5, -9, 20]
# convert = lambda num: abs(num)
# print(list(map(convert, l)))

# 4.. string starting with vowels
# ****************************************************************not done

# 5.. square and cube for list
# l = [2, 3, 4]
# sq_cu = lambda n: [n**2, n**3]
# print(list(map(sq_cu, l)))

# 6.. power index
# l = [2, 3, 4, 5]
# def power(num):
#     t1, t2 = num
#     return t2 ** t1
# print(list(map(power, enumerate(l))))

# 7.. sum of two list  ********************************************
# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 8]
# def sum(a, b):
#     return a+b
#
# print(list(map(sum, l1, l2)))

# 8.. print list len of each word
# s = "hi good afternoon"
# l = s.split()
# print(list(map(len, l)))

# 9.. return all letters in uppercase
# s = "hi good afternoon"
# l = s.split()
# print(list(map(str.upper, l)))

# ******************************************* FILTERS *********************************************************
# 1.. string starting with ovwels
# s = "apple, orange, mango, grapes"
# l = s.split()
# def vowels(s):
#     if s[0] in "aeiou":
#         return s
#
# print(list(filter(vowels, l)))

# 2.. print odd number range of 1 to 50
# l = range(1, 51)
# def num(i):
#         if i % 2 != 0:
#             return i
# print(list(filter(num, l)))

# 3.. return a list of string with odd length
# l = ["google", "chrome", "ttt"]
# def odd(n):
#     if len(n) % 2 != 0:
#         return n
# print(odd(list(filter(odd, l))))

# 4.. filter only positive value in the list
# l = [-5, -2, 3, 8]
# def pos(n):
#     if n > 0:
#         return n
# print(list(filter(pos, l)))

# 5 .. print prime number from 1 to 50
# l = range(1, 51)
# def prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return  n
# print(list(filter(prime, l))),
