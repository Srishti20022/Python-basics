a = 14
b = 28
multiple = 6
# print(str(14) + ' '+str(28)+' ', end = '')
value = 28
i = -1
flag = 1
n = 100
while value < n:
    if flag == 1:
        i = i + 1
        a = value = a + (6*i)
        flag = -1
    elif flag == -1:
        value = b = a * 2
        flag = 1
    print(value, end = ' ')