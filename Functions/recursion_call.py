# Reverse a string using recurssion ********************************
# s1 = "hello"
# def rec_rev(s):
#     if len(s) == 0:
#         return s
#     else:
#         return rec_rev(s[1:]) + s[0]
# print(rec_rev(s1))

# Factorial using recurssion ************************************
# def fact(n):
#     for _ in range(1, n):
#         f =  * n-1
#     return f
#     # print(f)
# # fact(5)
# print(fact(5))

# Recursive program from 10 to 1 **********************************
# # n = range(10, 1)
# def rec(n):
#     if n <= 10:
#         rec(n+1)
#         print(n)
#
# rec(5)

# sum of number using while loop *********************************************
# n = 123
# i=0
# while n > 0:
#     d = n%10
#     i = i+d
#     n = n//10
# print(i)

# using recursion
# def rec_sum(n, i=0):
#     if n > 0:
#         d = n % 10
#         i = i + d
#         n = n // 10
#         return rec_sum(n, i)
#     else:
#         return i

# print(rec_sum(1234))

# Fibonacci ******************************************
# n1 = 0
# n2 = 1
# for i in range(10):
#     print(n1, end=' ')
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
# print(fib(5))

# using recursion
def fib(n, n1=0, n2=1):
    if n > 0:
        print(n1, end=' ')
        n1, n2 = n2, n1 + n2
        return fib(n-1, n1, n2)
    else:
        return

fib(5)


