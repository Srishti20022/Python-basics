#Split function
# Syntax
# string-name.split(separator, max-split)
# Returns list of type string
string = "a b c d e f"
print("\n\n\n"+string)
print("Splitting of string with ' ' as separator and no maxsplit : "+str(string.split(" ")))
print("Splitting of string with ' ' as separator and 5 maxsplit : "+str(string.split(" ", 5)))

string1 = "a,b,c,d,e,f"
print("\n\n\n"+string1)
print("Splitting of string with ',' as separator and no maxsplit : "+str(string1.split(",")))
print("Splitting of string with ',' as separator and 4 maxsplit : "+str(string1.split(",", 4)))

string2 = "a-b-c-d-e-f"
print("\n\n\n"+string2)
print("Splitting of string with '-' as separator and no maxsplit : "+str(string2.split("-")))
print("Splitting of string with '-' as separator and 2 maxsplit : "+str(string2.split("-", 2)))


# Join function
# Syntax
# string-name.join(iterable)
# returns string concatenated
#iterable is a list
#whose elements are concatenated usiing string-name string
# Basically it is reverse of the split function
list = ['a', 'b', 'c', 'd', 'f']
print("\n\n\nJoining string using ' ' as iterator : "+" ".join(list))
print("Joining string using ',' as iterator : "+",".join(list))
print("Joining string using '-' as iterator : "+"-".join(list))