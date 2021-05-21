# Program to get a string made of the first two and the last two chars given in the string


def string1(s):
    length = len(s)
    if length < 2:
        return "Empty String"
    return s[0:2]+s[length-2:length]


a = input()
print(string1(a))