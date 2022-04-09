# 1.. WAF to count the number of positional and keyword arguments passed to it *********************
# def no_of_args(*args, **kwargs):
#     print(len(args))
#     print(len(kwargs))
#
# no_of_args(1, a=10, b=20)

# # 2.. WAF to print message "hai everyone" if user not present, if present display user input **********************
# def user_present(msg="hello everyone"):
#     print(msg)
#
# user_present(msg = "Hello India")

# 3.. check positional args passed more than 5
# def check_arg(*args):
#     if len(args) > 5:
#         print("more than 5")
#     else:
#         print("less than 5")
#
# check_arg(1, 2, 3)

# 4.. WAF to check list of even numbers from 1 to 10
# l = []
# def even(s, e):
#     for i in range(s, e):
#         if i % 2 == 0:
#             l.append(i)
#     return l
#
# print(even(1, 10))

# 5.. WAF return a dictionary to element and its count in any sequence **************************
# d = {}
# def count_element(sequence):
#     for item in sequence:
#         if item not in d:
#             d[item] = 1
#         else:
#             d[item] += 1
#     print(d)
#
# count_element("hello")

# 6.. WAF to return a list of first n prime numbers ************************************

# def n_prime(n):
#     l = []
#     count = 0
#     num = 0
#     while count < n:
#         if num > 1:
#             for i in range(2, num):
#                 if num % i == 0:
#                     break
#             else:
#                 count += 1
#                 l.append(num)
#         num += 1
#     return l
# print(n_prime(5))

# 7.. check if the given number is prime or not?
# def check_prime(n):
#         for i in range(2, n):
#             if n % 2 == 0:
#                 print("not prime")
#                 break
#         else:
#             print("prime")
#
#
# check_prime(8)

# 8.. WAF to return last digit of any number
# def last_dig(num):
#     x = str(num)
#     y = x[-1]
#     return int(y)
#
# res = last_dig('123451')
# print(res)

# 9.. WAF named tail take a sequence and number the last n ele given seq
# def tail(sequence, n):
#     return list(sequence[-n:])
#
# print(tail("hello", 3))

# 10.. WAF return only the ele which are starting with vowels in thr given list
# s = "today is tuesday"
# def vowels(s):
#     l = []
#     for i in s:
#         if i[0] in "aeiouAEIUO":
#             l.append(i)
#     return l
#
# list_sp = s.split()
# print(vowels(list_sp))

# # 11.. WAF to check if given number is fibonacci or not
# def check_fibonacci(n):
#     a = 0
#     b = 1
#     while a <= n:
#         if a == n:
#             return "fibonnaci"
#         c = a + b
#         a = b
#         b = c
#     return "not fibonacci"
#
# print(check_fibonacci(1))




