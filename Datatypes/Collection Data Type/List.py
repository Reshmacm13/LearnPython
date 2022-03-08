# *************Adding element to list******************
# append
import copy

l = [10, 20, 30, 40, 50]
# l1 = l.append([30, 40])
# print(l)

# extend
# l2 = l.extend([40, 50])
# print(l)

# insert
# l3 = l.insert(3, 100)
# print(l)

# *********************Removing element from list*********************
# POP
# l4 = l.pop(0)
# print(l4)

# remove
# l5 = l.remove(20)
# print(l)

# del
# l6 = del l[10]            # Not working
# print(l)

# ********************** Copy ****************************************
# a = [1, 2, 3, 4, 5]
# b = a.copy()
# print(b)

# n = [120, 130]
# x = copy.deepcopy(n)
# print(x)

# **********************Sort Lists ***********************************
# Sort
names = ["Infosys", "Google", "Microsoft", "Accenture", "Phillips", "Google"]
# names.sort()
# print(names)

# Sort in Reverse order
# names.sort(reverse=True)
# print(names)

# Sort in key len
# names.sort(key=len)
# print(names)

# ********************** Index **************************************
# print(names.index("Google"))
# print(names.index("flip"))

# ********************** count **************************************
# print(names.count("Google"))
# print(names.count("flip"))

# ********************** Constructing from list to string/viceversa *************
# Using split and join ============
s = "hai how are you"
# l = s.split()
# print(l)
# s1 = " ".join(l)
# print(s1)

# Using list constructor and join ============
l = list(s)
print(l)
s2 = "".join(l)
print(s2)
