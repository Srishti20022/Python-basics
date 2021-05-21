tup = (1, 2, 3, 5, 4, 6)
print("Tuples before value is changed : ", end="")
print(tup)
# as tuples are immutable unlike lists so we cannot change the values of elements in the tuples
# tup[3] = 4 These two lines would show error
# tup[4] = 5
print("Tuples after some values are changed : "+str(tup))
length = len(tup)
print("The length of tuple is : "+str(length))


a = (0, )
print("Tuples before appending any other tuples to it : "+str(a))
a = a+tup
#a.append(tup)
print("Tuples after appending "+str(tup)+" to it : "+str(a))
b = (7, 8, 9, 10)
a = a+b
# a.append(5)
print("Tuples after appending "+str(b)+" to it : "+str(a))
# this will show error as tuples are immutable so we cannot change value we cannot add element to it by using append or extend method we cannot xtend or append it
