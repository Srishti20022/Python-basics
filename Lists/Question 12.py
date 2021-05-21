def indexOfSmallestElement(lst):
    min = lst[0]
    for i in lst:
        if i < min:
            min = i

    if min > 1:
        return 0
    else :
        return min


str = input()
list = str.split(" ")
list  = [int(i) for i in list]
print(indexOfSmallestElement(list))
