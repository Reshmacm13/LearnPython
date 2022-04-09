#1.. List of even numbers between range 1-50
# def even_(list_):
#     for n in list_:
#         if n % 2 == 0:
#             yield n
#
# print(list(even_(range(1, 51))))
#
# # generator expression
# numbers = range(1, 51)
# evens = (n for n in numbers if n % 2 == 0)
# print(list(evens))

# 2.. Returns a list names starting with vowels in the given string
names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']

# def vowels_(s):
#     for i in s:
#         if i[0] in 'aeiouAEIOU':
#             yield i
#
# print(list(vowels_(names)))
#
#
# # generator expression
# vowel = [i for i in names if i[0] in "aeiouAEIOU"]
# print(vowel)

# 3.. Filtering all the languages which starts with 'p'
languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']

# def lang_(s):
#     for i in s:
#         if i[0] in 'P':
#             yield i
#
# print(list(lang_(languages)))
#
# # generator expression
# l = [i for i in languages if i[0] in "P"]
# print(l)

# 4.. Names starting with consonants
# names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']
# def const_(s):
#     for i in s:
#         if i[0] not in 'aeiouAEIOU':
#             yield i
#
# print(list(const_(names)))
#
#
# # generator expression
# const = [i for i in names if i[0] not in "aeiouAEIOU"]
# print(const)

# 5.. Filtering out those names which are less than 6 characters

# names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']
# def name_(list_):
#     for i in list_:
#         if len(i) < 6:
#             yield i
#
# print(list(name_(names)))
#
#
# # generator expression
# n = (i for i in names if len(i) < 6)
# print(list(n))

# 6.. Raise to the power of list index
# a = [1, 2, 3, 4, 5]
#
# def pow_(list_):
#     for index, value in enumerate(list_):
#         b = value ** index
#         yield b
#
# print(list(pow_(a)))
#
# # generator expression
# p = (value ** index for index, value in enumerate(a))
# print(list(p))

# 7.. Build a list of tuples with string and its length pair
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

def count_(list_):
    for index, value in enumerate(list_):
        value = len(value)
        return value

print(count_(names))