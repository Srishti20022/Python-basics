def rangec(a, r1, r2):
    count = 0
    for i in a:
        if r1 < i < r2:
            count = count + 1
    return count


a = (1, 5, 2, 8, 0)
print("Finding minimum and maximum value without sorting the tuple : "+str(a))
min = a[0]
max = a[0]
for i in a:
    if i < min:
        min = i
    if i > max:
        max = i
print("Minimum value : "+str(min))
print("Maximum value : "+str(max))
lst = []
lst = [int(i) for i in a]
lst.sort()
b = (lst[0], )
length = len(lst)
for i in range(1, length):
    b = b + (lst[i], )
a = b
print(a)
sum = 0
for i in a:
    sum = sum + i
print("The sum of all elements of tuple is : "+str(sum))
print("Finding minimum and maximum element with sorted array : "+str(a))
print("Maximum value : "+str(a[0]))
print("Minimum value : "+str(a[length - 1]))
print("Write the range i which values of the tuple to be counted(Both exclusive) : ",end='')
c, d = input().split(" ")
c = int(c)
d = int(d)
print("Count : "+str(rangec(a, c ,d)))