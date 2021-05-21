# to compare time and space took by array and list
import numpy as np
import time
import sys
list_1 = list(range(1000))
# get size functions used to get size of any function
print("size of lst : ", end = ' ')
print(sys.getsizeof(list_1))
array_1 = np.array(list(range(1000)))
array_2 = np.array(list(range(1000)))
print("size of array : ", end = ' ')
print(sys.getsizeof(array_1))
list_2 = list(range(1000))
start = time.time()
for i in range(len(list_1)):
    list_1[i]+list_2[i]
end = time.time()
total = end - start
print("total time for lists: "+str(total))
start = time.time()
array_1+array_2
end = time.time()
total = end - start
print("total time for array:"+str(total))