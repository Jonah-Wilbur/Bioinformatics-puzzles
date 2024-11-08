import numpy as np
def GC(seq):    
    return (100*(seq.count('G')+seq.count('C'))/(len(seq)-seq.count(' ')))
k=0
name=[]
sequence=[]
GC_index=[]
while True:
    name.append(input())
    if(name[-1]==' '):
        break
    sequence.append(input())
    GC_index.append(GC(sequence[-1]))
point=np.argmax(GC_index)
a=name[point]
print(a[1:])
print(GC_index[point])
print(name)
print()