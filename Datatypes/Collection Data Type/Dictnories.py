# ********************Creating python Directory*****************

# empty dictionary
d = {}

# dictionary with integer keys
d = {1: 'apple', 2: 'ball'}

d = {'name': 'John', 1: [2, 4, 3]}

# ******************* Acessing values from a directory using get and [] *****************
d = {'name': 'Jack', 'age': 26}

print(d['name'])
print(d.get('age'))
# print(d['test'])   # value not present return --> error
print(d.get('test'))  # value not present return --> NOne


# ******************* Adding and updating the directory  *******************************

d = {'name': 'Jack', 'age': 26}

d['age'] = 27
d['address'] = 'bangalore'
print(d)

# ******************* Removing elements from a dictionary *******************

# create a dictionary
s1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
print(s1.pop(4))
# print(s1.pop(14))   #keyerror
print(s1.popitem())      # remove key and value


# ********fromkeys(seq[, v])	Returns a new dictionary with keys from seq and value equal to v (defaults to None).


