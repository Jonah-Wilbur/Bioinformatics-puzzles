from itertools import permutations 
import math
n=int(input())
array = []
for i in range(n):
    array.append(i+1) 
     
perm = permutations(array)  
print(math.factorial(n))
for i in list(perm): 
    print (i[0], i[1], i[2], i[3], i[4], i[5])