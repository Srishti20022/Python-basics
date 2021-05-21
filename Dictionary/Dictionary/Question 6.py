a = dict() # dictionary
a['1'] = ['a', 'b']
a['2'] = ['c', 'd']
# fom this program we could only unpack two values
from itertools import product

for x, y in product(*a.values()):
    print(x + y)