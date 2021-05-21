# To merge two python dictionaries
dict1 = {3: 9, 1: 1, 5: 25}
dict2 = {10: 100, 1: 1, 2: 4, 15: 225}
dict3 = {}
dict3.update(dict1)
dict3.update(dict2)
a = sorted(dict3)
print(dict3)
# Dictionary does not allow duplicate keys
# Sum of all elements
#Question 7, 8
multiply = 1
sum = 0
for i in a:
    sum = sum + dict3[i]
    multiply = multiply*dict3[i]
print('Sum : '+str(sum))
print('Multiply : '+str(multiply))
# Question 9
# Key to be removed
remove = 3
del dict3[remove]
print(dict3)
# Question 10
dict4 = {3: 9, 1: 1, 5: 25, 10: 100, -1: 1, -5: 25, -10: 100, 2: 4, 15: 225}
# To remove duplicate elements from dictionary(Specifically keys)
temp = []
test = dict() # To form empty dictionary
print('Dictionary before removal of duplicate elements : '+str(dict4))
# We are storing the values of keys in the list temp which are not already stored in list and then
for key, val in dict4.items():
    if val not in temp:
        temp.append(val)
        test[key] = val
print('Dictionary : '+str(test))