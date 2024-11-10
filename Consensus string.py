import numpy as np
import array

def interspace(arr):
    arr = arr.astype(object)
    for i in range(len(arr) - 1, 0, -1):  # Start from the end and move backward
        arr = np.insert(arr, i, ' ')
    return arr
def remove_spaces(string):
    output = ''
    for i in range(len(string)):
        if string[i]!=' ':
            output = output + string[i]
    return output
def concensus_element(strand):
    A=[]
    C=[]
    G=[]
    T=[]
    for i in range(len(strand)):
        if strand[i]=='A':
            A.append(1)
            C.append(0)
            G.append(0)
            T.append(0)
        if strand[i]=='C':
            A.append(0)
            C.append(1)
            G.append(0)
            T.append(0)
        if strand[i]=='T':
            A.append(0)
            C.append(0)
            G.append(0)
            T.append(1)
        if strand[i]=='G':
            A.append(0)
            C.append(0)
            G.append(1)
            T.append(0)
        #A.append(' ')
        #C.append(' ')
        #G.append(' ')
        #T.append(' ')
    return [A, C, T, G]

def concensus_string(list):
    A=concensus_element(list[0])[0]
    C=concensus_element(list[0])[1]
    T=concensus_element(list[0])[2]
    G=concensus_element(list[0])[3]
    for i in range(1, len(list), 1):
        A=np.add(A,concensus_element(list[i])[0])
        C=np.add(C,concensus_element(list[i])[1])
        T=np.add(T,concensus_element(list[i])[2])
        G=np.add(G,concensus_element(list[i])[3])
    return [A, C, T, G]

def ancestor(concencus):
    anc=[]
    for i in range(len(concencus[0])):
        numbers= [arr[i] for arr in concencus]
        if np.argmax(numbers)==0:
            anc.append('A')
        if np.argmax(numbers)==1:
            anc.append('C')
        if np.argmax(numbers)==2:
            anc.append('T')
        if np.argmax(numbers)==3:
            anc.append('G')
    return ''.join(anc)
strand=[]
while True:
    a=input()
    if a==' ':
        break
    strand.append(remove_spaces(a))

A=concensus_string(strand)[0]
C=concensus_string(strand)[1]
T=concensus_string(strand)[2]
G=concensus_string(strand)[3]

A=interspace(A)
C=interspace(C)
T=interspace(T)
G=interspace(G)


AA=''.join(str(x) for x in A)
CC=''.join(str(x) for x in C)
TT=''.join(str(x) for x in T)
GG=''.join(str(x) for x in G)
print(ancestor(concensus_string(strand)))
print('A:' , AA)
print('C:' , CC)
print('T:' , TT)
print('G:' , GG)
#how to find max of first element of several arrays