# Reversing the tuple
def reverset(a, length):
    t = ()
    for i in range(length-1, -1, -1):
        t = t+(a[i], )
    return t


print("Write the elements of the tuples(space separated) : ", end=" ")
lst = input().split(" ")
tple = tuple(lst)
l = int(len(lst))
print("Entered tuple : "+str(tple))
tple = reverset(tple, l)
print("Reversed tuple : "+str(tple))
for i in tple:
    print("Length of : "+str(i)+" is : "+str(len(i)))


