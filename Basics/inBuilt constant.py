a = None
b = Ellipsis
c = NotImplemented
d = ... # also ellipses
if a is None : # to check whether a is none or not
    print('abc')
k = 'hello'
kl = list(k) # ['h', 'e', 'l', 'l', 'o'] immutable
ks = set(k) # {'o', 'e', 'l', 'h'} unique value, unodered
kt = tuple(k) #('h', 'e', 'l', 'l', 'o') mutable
print(kl)
print(ks)
print(kt)
print(type(d))
help(type)