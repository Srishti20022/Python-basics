# Calculate UpperCase or LowerCase


def count(s):
    import string
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    countu = 0
    countl = 0
    for i in s :
        if i in lower:
            countl += 1
        elif i in upper:
            countu += 1

    print("Lowercase : "+str(countl))
    print("UpperCase : "+str(countu))


a = input()
count(a)