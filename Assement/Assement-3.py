# 1.. create a list with item list have even number of characters and comphrensions ***************
# names = ["apple", "yahoo", "google", "gmail", "walmart", "flipkart", "facebook", "amazon"]
# l = []
# for i in names:
#     if len(i) % 2 == 0:
#         l.append(i)
# print(l)
#
# # comphrensions
# l = [i for i in names if len(i) % 2 == 0]
# print(l)

# 2.. get only duplicate elements in list
# names = ["apple", "google", "apple" "yahoo", "google"]
# dup = []
# count = 0
# for i in names:
#     if names.count(i) > 1:
#         count += 1
#         dup = [i]
# print(dup)
#
# # comprehensions
# dup = [i for i in names if names.count(i) > 1]
# print(dup)


# 3.. Create a dictionary of words and count pair
# words = ['Hi', 'How', 'are', 'you', 'my', 'How', 'are', 'you']
# d = {}
# for i in words:
#    # d[i] = len(i)
#    if i not in d:
#        d[i] = 1
#    else:
#        d[i] += 1
# print(d)
#
# # comphrension
# d = {i : 1 if i not in d else 1 for i in words}
# print(d)

# 4..  Write a list comprehension to create a list to reverse the item of a list if the item is of odd
# length string else keep it as it is.
# names = ['apple’, ‘google’, ‘yahoo’, ‘facebook’, ‘yelp’, ‘flipkart’, ‘gmail’, instagram’, ‘microsoft']
# l = []
# for i in names:
#     if len(i) % 2 == 0:
#         l.append(i)
#     else:
#
#         l.append(i[::-1])
# print(l)

# 5.. Create a dictionary with the first character and the name pair only if the names are
# starting with vowels in the given string :
# names = [laura’, ‘steve’, 'bill’, james’, 'bob', ‘greig’, ‘scott’, ‘alex’, ‘ive’]


