# Taking input of a tuple numbers ar separated by space
lst = input().split(" ")
tple = tuple(lst) # explicit conversion
print(str(lst)+"list")
print(str(tple)+"tuple")

# creatimg an empty tuple
tple = ()
a = (1, 2, 3)
b = (4, 5, 6)
c = (7, 8, 9)
# Tuples
# As the variables value changed are new variables which store the values of a and b not a and b itself
def swap(x, y):
    x,y = y, x
    print(x, end=":  x\n")
    print(y, end=":  y\n")
swap(a, b)
print(a, end=":  a\n")
print(b, end=":  b\n")
print(c, end=":  c\n")

#random.random() returns random no. between 0.0 to 1.0
import random
for i in range(20):
    print((int)(random.random()*100))
a, b, c = c, b, a
print("After swapping values")
print(a, end=":  a\n")
print(b, end=":  b\n")
print(c, end=":  c\n")
