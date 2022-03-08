# *********************** program to print vowels ****************************
# s = "hello world"
# i = 0
#
# while i < len(s):
#     if s[i] in "aeiouAEIOU":
#         print(f"{s[i]} is a vowels")
#     else:
#         print(f"{s[i]} not vowels")
#     i += 1

# ************************ program to print from 10 t0 1 **********************
# i = 0
# while i <= 10:
#     print(i)
#     i += 1

# i = 10
# while i >= 0:
#     print(i)
#     i -= 1

# ************************ program to print even range from 1 to 20 *******************
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i+=1

# ************************* print even or odd ****************************
# n = [1, 2, 3, 4, 5]
# i = 0
# while i < len(n):
#     if n[i] % 2 == 0:
#         print("its even num")
#     else:
#         print("its odd num")
#     i += 1

# ************************ program from -1 to -10 ***************************
# i = -1
# while i >= -10:
#     print(i)
#     i -= 1

#  *********************** print all characters/elements in an iterable ***************
# Using string
# c = "hai"
# i = 0
# while i < len(c):
#     print(c[i])
#     i += 1

# Using list
# l = [10, 20, 30, 40, 50]
# i = 0
# while i < len(l):
#     print(l[i])
#     i += 1

# Using Tuples
# t = (1, 2, 3, 4, 5)
# i = 0
# while i < len(t):
#     print(t[i])
#     i +=

# *********************** print string in reverse order **********************
# method1
# s = "python"
# i = len(s)-1
# while i >= 0:
#     print(s[i], end='')
#     i -= 1

# method2
# res = ''
# n = 0
# while n < len(s):
#     res = s[i] + res
# i += 1
# print(res)

# ********************* print element and its index in given sequence ***************
# l = ["google", "amazon", "flipkart", "phillips"]
# i = 0
# while i < len(l):
#     print(i, l[i])
#     i += 1

# ********************** print odd index character in string ********************
# s = "myworld"
# i = 0
# while i < len(s):
#     if i % 2 != 0:
#         print(i, s[i])
#     i += 1

# ************************ print only numeric values in given string ************
# method1
s = "reshma1311kc"
i = 0
# while i < len(s):
#     if s[i].isdigit():
#         print(s[i])
#     i += 1

# method2
# while i < len(s):
#     if "1" <= s[i] <= "9":
#         print(s[i])
#     i +=1

# *************** count number of lower case alphabets in string *******************
# # lowercase
# s = "Hi Namaste"
# count = 0
# i = 0
# while i < len(s):
#     if "a" <= s[i] <= "z":
#         count += 1
#         print(s[i], end='')
#     i += 1
# print()
# print("count is:", count)

# uppercase
# s = "Hi Namaste"
# count = 0
# i = 0
# while i < len(s):
#     if "A" <= s[i] <= "Z":
#         count += 1
#         print(s[i], end='')
#     i += 1
# print()
# print("count is:", count)

# ******************************* count digits in given string ***********
# s = "Namaste karnataka 15-08-1947"
# i = 0
# count = 0
# while i < len(s):
#     if "0" <= s[i] <= "9":
#         count = count + int(s[i])
#     i += 1
# print(count)





