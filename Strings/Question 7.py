# Add ing to the string at the end of the given string
# String remains unchanged if the length of string is less than three


def ing(s):
    length = len(s)
    if length < 3:
        return s
    return s[0:length] + "ing"


a = input()
print(ing(a))