import numpy as np
def C(DNA):
    limit=len(DNA)
    Complement=''
    for i in range (limit):
        if Leading_strand[i]=='A':
            Complement=Complement+'T'
        if Leading_strand[i]=='T':
            Complement=Complement+'A'
        if Leading_strand[i]=='C':
            Complement=Complement+'G'    
        if Leading_strand[i]=='G':
            Complement=Complement+'C'
    return Complement
def R(str):
    limit=len(str)
    Reverse=''
    i=1
    for i in range(limit+1):
        Reverse=Reverse+str[-i]
    return Reverse[1:]

Leading_strand=input()
Complement=C(Leading_strand)
Reverse=R(Complement)
print(Reverse)