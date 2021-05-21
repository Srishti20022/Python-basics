# To compare elements of two lists
print("Enter 1st list : ")
lst1 = input().split(" ")
print("Enter 2nd list : ")
lst2 = input().split(" ")
# Using list comprehension method to convert the string elements of list to integer
lst1 =[int(i) for i in lst1]
lst2 = [int(i) for i in lst2]
flag = 0
lst1.sort()
lst2.sort()
length = len(lst1)
for i in range(0, length):
    if lst1[i] != lst2[i]:
        print("False")
        flag = 1
        break

if flag == 0:
    print("True")
