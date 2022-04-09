s ="NaMaStE"
for i in s:
    if "a" <= i <= "z":
        upper_ = chr(ord(i) - 32)
        print(upper_)
    elif "A" <= i <= "Z":
        low_ = chr(ord(i) + 32)
        print(low_)

