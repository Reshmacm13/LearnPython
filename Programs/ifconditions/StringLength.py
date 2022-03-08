l = "reshma"
d = {}

if len(l) % 2 == 0:
    d[l] = ord(l[0])
    print(d)
else:
    d[l] = len(l)
    print(d)
