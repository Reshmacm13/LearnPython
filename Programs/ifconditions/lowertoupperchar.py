c = "&"
if c.isupper():
    print("is upper")
elif c.islower():
    print("is lower")
else:
    print("character is not alphabets")

# ************** without using inbuilt fun ****************
char = "b"
if "a" <= char <= "z":
    upper_ = chr(ord(char) - 32)
    print(upper_)
elif "A" <= char <= "Z":
    print(chr(ord(char) + 32))
else:
    print("character is not an alphabet")