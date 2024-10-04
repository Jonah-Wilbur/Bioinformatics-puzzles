import numpy as np

pairs=[0]
new_pairs=[1]
m=int(input())
litter=int(input())
for i in range (m-1):
    pairs.append(pairs[i]+new_pairs[i])
    new_pairs.append(pairs[i]*litter)
    
print(pairs[-1]+new_pairs[-1])