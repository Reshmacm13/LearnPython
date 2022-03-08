x = "atest"
d = {}

# print(len(x))
if x[0] in "aeiouAEIOU":
    print("vowels")
    d[x] = len(x)
    print(d)
else:
    print(" not vowels")