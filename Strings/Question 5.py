# frequency of particular character


def find(s, f):
    count = 0
    for i in s:
        if i == f:
            count +=1
    return count


print("Write the string whose frequency to be checked : ", end="")
s1 = input()
print("Write the character whose frequency to be counted : ", end="")
a1 = input()
print("Occurence : "+str(find(s1, a1)))