# Takes list of the words and return the length of the longest one

def longest(lst):
    max = len(lst[0])
    for i in lst:
        length = len(i)
        if length > max:
            max = length
    return max


lst = []
n = int(input("Enter size of the list : "))
print("Write elements of the list")
for i in range(0, n, 1):
    ele = (input())
    lst.append(ele)
print(longest(lst))
