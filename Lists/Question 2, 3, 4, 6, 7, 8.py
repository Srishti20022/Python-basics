list = [11, 9, 10, 5]
print("Original list : "+str(list))
print("Write two numbers to be inserted in the list : ")
list.append(int(input()))
print("Appended list : "+str(list))
list.append(int(input()))
print("Appended list : "+str(list))
list.sort()
print("Sorted list : "+str(list))

sum = 0
max = list[0]
min = list[0]
for i in list:
    sum += i
    if i > max:
        max = i
    if i < min:
        min = i
print("Sum of list elements : "+str(sum))
print("Minimum element of list : "+str(min))
print("Maximum element of list : "+str(max))

print("Write the number whose occurrence is to be measured : ")
a = int(input())
count = 0
for a in list:
    if a == i:
        count +=1
print("occurrence of number "+str(a)+" is : "+str(count))

# reversing the list
length = len(list)
for i in range(0, int(length/2)):
    s = list[i]
    list[i] = list[length-i-1]
    list[length-i-1] = s
print("Reverse of list : "+str(list))