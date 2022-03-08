# ****************** Using inbuilt function *****************
c = "r"
if c.isalpha():
    print(f"{c} is alphabets")
elif c.isdigit():
    print(f"{c} is number")
else:
    print(f"{c} is special character")

# ****************** without Using inbuilt function *****************
char = "r"
if ("a" <= char <= "z") or ("A" <= char <= "Z"):
    print(f"{char} ---> characters is a alphabet")
elif "0" <= char <= "9":
    print("character is number")
else:
    print("character is a special character")