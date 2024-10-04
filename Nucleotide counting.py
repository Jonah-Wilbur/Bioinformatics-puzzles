import numpy as np

Sequence=input()
limit=len(Sequence)
i=0
A=0
T=0
C=0
G=0
for i in range (limit):
    if Sequence[i]=='A':
        A=A+1
    if Sequence[i]=='T':
        T=T+1
    if Sequence[i]=='C':
        C=C+1
    if Sequence[i]=='G':
        G=G+1
print(A, C, G, T)
