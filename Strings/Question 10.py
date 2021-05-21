def change(s):
    char = s[0]
    length = len(s)
    for i in range(1, length):
        if s[i] == char:
            s = s[0:i]+"$"+s[i+1:]
    s = char+s[1:]
    return s


a = input("Write the string : ")
print(change(a))