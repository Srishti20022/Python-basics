# a = -1
# print(a)
# print(type(a))
# pi = 3.14
# print(type(pi))
# a, b, c, d = 1, 2, 3, 4
# print(a)
# print(b)
# print(c)
# print(d)
# a = b = c = 1
# print(a)
# print(b)
# print(c)
# x = y = [1, 2, 3]
# x[0] = -1
# print("x : "+str(x))
# print("y : "+str(y))
# # Value changed is reflected
# x = [12, 23, 32]
# print("x : "+str(x))
# print("y : "+str(y))
# # list name is changed
# print(issubclass(bool, int))
# # print(issubclass(1, int)) Shows error as both should be classes that should be checked
# # print(issubclass(str, 'int')) Same as above
#print(issubclass(bool, bool))
## print(issubclass(True, bool))
# a1 = 123.e100
# print(a1)
# w = 1 + 8j#complex number
# print(w)
# aq = b'abchshdjfh'
# print(bytes.decode(aq))
a = 'acdefghijklmno'
q = (reversed(a))
print("q : "+str(q))
print("*q : ", end ="")
print(*q)
print(type(q)) # q is an object of class reversed
print(list(reversed(a)))# now print a list as iterator could be converted to list or tuple
