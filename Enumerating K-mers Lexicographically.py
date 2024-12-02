from itertools import product
from math import factorial
alphabet=input()
n=int(input())
arr=[]
for i in range(len(alphabet)):
    arr.append(alphabet[i])
combo = product(arr, repeat=n)  
#print(int(len(alphabet)**n/factorial(n)))
for i in list(combo):
    a=''
    for j in range(n):
        a=a+(i[j])
    print(a)