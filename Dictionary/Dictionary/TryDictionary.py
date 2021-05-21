#Dictionary are basically key value pair
d1 = {'one': 1, 'two': 2, 'three': 3, 'four': 4 }
print("d1 : "+str(d1))
print(d1['one'])
d2 = {'fruit':'mango', 1 : 'one', 'two': 2}
print("d2 : "+str(d2))
print(d2['fruit'])
d3 = {'one': [1, 2, 3], 'two': [3, 4, 5, 6]}
print(d3['one'])
# Deletion of element
del d3['one']
print("d3 : "+str(d3))
del d3['two']
print('d3 : '+str(d3))
# To print all the keys of dictionary
print(d2.keys())
# To print all the value of dictionary
print(d2.values())
# To print all the items of the dictionary
print(d2.items())
# Assignment of one dictionary to another dictionary
d3 = d2
print('d2 : '+str(d2))
print('d3 : '+str(d3))
del d2['fruit']
# deletion is reflected in dictionary d2 also so this implies that both d2 and d3 have same
# memory address
print('d3 : '+str(d3))
# NOW we are creating a new memory address to store the same values of previous dictionary
d1 = d2.copy()
print('d1 : '+str(d1))
print('d2 : '+str(d2))
# Finding minimum and maximum of dictionary
my_dict = {'a':1, 'b':87, 'd':2, 'c':-1}
key_mix = min(my_dict.keys(), key = (lambda k: my_dict[k]))
print(key_mix)
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic4 = {}
for d in (dic1, dic2, dic3) : dic4.update(d)
print(dic4)
