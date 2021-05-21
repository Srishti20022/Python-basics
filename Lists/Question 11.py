print("Enter 10 Numbers : ", end="")
str = input()
list = str.split(" ")
list2 = []
length = len(list)
print("The distinct Numbers are ", end="")
for i in range(0, length, 1):
    flag = 0
    element = list[i]
    for j in range(i+1, length, 1):
        if element == list[j]:
            flag = 1
            break
    if flag == 0:
        list2.append(element)

list2.sort()
for k in list2:
    print(k, end=" ")