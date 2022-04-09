# l = [1, 2, 3, 4, 5]
# for i in range(0, len(l), 2):
#     print(l[i: i+2])
#
# l = [i for i in range(1, 51) if i % 2 == 0]
# print(l)
#
# s ="are hello world"
# l = [i for i in s.split() if i[0] in 'aeiou']
# print(l)

# s = "hello world"
# l = []
# for word in s.split():
#     i = word, len(word)
#     l.append(i)
# print(l)

# s = "hi how are you"
# l = [word if len(word) % 2 == 0 else word[::-1] for word in s.split()]
# print(l)

# s = "hello world"
# d = {i: len(i) for i in s.split()}
# print(d)

# s = "hello word hai"
# d = {j:len(j) if len(j) % 2 == 0 else j[::-1] for i, j in enumerate(s.split())}
# print(d)

# def count_(*args, **kwargs):
#     print(len(args))
#     print(len(kwargs))
#
# count_(5, 6, a= 10, b= 20, c=30)

# def greet(msg = "Hello"):
#     print(msg)
#
# greet("test")

# def even_(l):
#     for i in l:
#         if i % 2 == 0:
#             print(i, end=",")
#
#
# l = range(1, 11)
# even_(l)

# s = ["Hello", "World"]
# print(' '.join(s))
#
#
# s1 = "Hi world"
# print(s1.split())

# 18 write a decorator that returns only positive values of subtraction**

# l = lambda a, b: a+b
# print(l(10, 20))
#
#
# a = [1, 2, 3]
# b = [4, 5, 6]
# print([a, b])
# print((a, b))

# items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# l = []
# for i in items:
#     if i not in l:
#         l.append(i)
# print(l)

# t = ('1', '2', '3', '4')
# print(''.join(t))

s = ""

*a = 10
print(*a)