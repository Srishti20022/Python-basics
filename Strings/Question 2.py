# Palindrome or not


def checkP(s):
    length = int(len(s))
    flag = True
    for i in range(0, int(length/2)+1, 1):
        if s[i] != s[length - 1 - i]:
            flag = False
            break
    return flag


print("Write the string to check whether it is palindrome or not :  ", end="")
str1 = input()
print(checkP(str1), end="\n\n")