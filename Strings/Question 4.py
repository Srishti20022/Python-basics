import string

def panagram1(s):
    s = s.lower()
    a = string.ascii_lowercase
    for i in a:
        if i not in s:
            return False
    return True


print("Write string to check whether it is panagram or not : ")
a = input()
print(panagram1(a))