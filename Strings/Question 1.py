# reverse of string

# Using Loops
def reverse1(s):
    str1 = " "
    for i in s:
        str1 = i + str1
    return str1


# Using Recursion
def reverse2(s):
    if len(s) == 0:
        return s
    else:
        return reverse2(s[1:]) + s[0]


s = "GeeksForGeeks"
print(reverse1(s), end="\n")
