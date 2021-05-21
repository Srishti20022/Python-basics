print("Enter elements separated by " " ", end="")
lst = input().split(" ")
lst = [int(i) for i in lst]
n = len(lst)
sum = 0
for i in lst:
    sum += i
mean = sum/n
sum = 0
import math
for i in lst:
     sum += pow(i - mean, 2)
k = sum/(n)
sd = math.sqrt(k)
print("Mean of elements "+str(lst)+" is : "+str(mean))
print("Standard Deviation of elements "+str(lst)+" is : "+str(sd))