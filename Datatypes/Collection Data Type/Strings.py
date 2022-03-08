# lower
s = 'NAMASTE'
print(s.lower())

# upper
s1 = 'namaste'
print(s1.upper())

# count
print()
s2 = "Namaste karanataka"
print(s2.count('k'))
print(s2.count('k', 0, 20))

# find & rfind
print("********find**********")
print(s2.find('k'))
print(s2.rfind('k'))
print(s2.find('z'))

# Index() & rindex()
print()
print("********index**********")
print(s2.index('k'))
print(s2.rindex('k'))
# print(s2.index('universe'))        # ==============Not getting

# replace
print()
print("********replace**********")
r = "MANGOO"
print(r.replace('M', 'A'))
print(r.replace('Z', 'A'))
print(r.replace('O', 'S', 1))

# startswith & endswith
print()
print("********start & end**********")
e = "How are you"
print(e.startswith('How'))
print(e.startswith('are'))
print(e.endswith('you'))

# split
print()
print("******** split **********")
sp = "hello word day"
print(s2.split())
print(s2.split('k'))
print(sp.split(" ", 2))

# join
print()
print("******** join **********")
h = "Hello"
print('#'.join(h))
print(h.join(["Hi", "world"]))

# strip lstrip rstrip
print()
print("******** strip lstrip rstrip **********")
st = "***********hi======"
print(st.strip('='))
print(st.strip('*'))
print(st.strip('=*'))
print(st.lstrip('='))
print(st.rstrip('='))

# isalnum, isalpha, isdigit, islower, islower, isnumeric, isupper, isspace
print()
print("******** isalnum, isalpha, isdigit, islower, islower, isnumeric, isupper, isspace **********")
a1 = "1234"
a2 = "abcd"
print(a1.islower())
print(a1.isalpha())
print(a1.isdigit())
print(a1.isnumeric())
print(a1.isupper())
print(a1.isspace())