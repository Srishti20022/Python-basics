dic_1 = {1:10, 2:20}
dic_1[3] = 30 # where 3 is key and 30 is value
print(dic_1)
dic_2 = {4:40, 5:50, 6:60}
dic_3 = {7:70, 8:80, 9:90}
dic_4 = {}
dic_4.update(dic_1)
dic_4.update(dic_2)
dic_4.update(dic_3)
print(dic_4)
keyToBeChecked = 6
print()