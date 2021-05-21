print("Enter digits between 1 to 20 : ", end="")
lst = input().split(" ")
# Using list comprehension to perform conversions
lst = [int(i) for i in lst]
count = []
for i in range(0, 20, 1):
    count.append(0)
length = len(lst)
for i in lst:
    count[i-1] += 1

j = 0
for i in count:
    j += 1
    if i != 0:
        print(str(j)+" ocurrs "+str(i)+" times ")
