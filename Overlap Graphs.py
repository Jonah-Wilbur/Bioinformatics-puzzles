def FASTA_to_str(FASTA):
    string=''
    for i in range(len(FASTA)):
        if FASTA[i]!=' ':
            string=string+FASTA[i]
    return string
def prefix(s):
    string=str(s[0]+s[1]+s[2])
    return string
def suffix(s):
    string=str(s[-3]+s[-2]+s[-1])
    return string
def overlap(index, DNA):
    output=[]
    for i in range (0, len(DNA), 1):
        for j in range(i+1, len(DNA), 1):
            if prefix(DNA[i])==suffix(DNA[j]) or prefix(DNA[j])==suffix(DNA[i]):
                print(index[i], index[j])


name=[]
strands=[]
while True:
    a = input()
    if a[0]=='>':
        name.append(a[1:])
    elif a[0]==' ':
        break
    else:
        strands.append(FASTA_to_str(a))

overlap(name,strands)