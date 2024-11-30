def redundancies(aa):
    if aa=='A':
        return 4
    if aa=='C':
        return 2
    if aa=='D':
        return 2
    if aa=='E' :
        return 2
    if aa=='F':
        return 2
    if aa=='G':
        return 4
    if aa=='H':
        return 2
    if aa=='I':
        return 3
    if aa=='K' :
        return 2
    if aa=='L':
        return 6
    if aa=='M':
        return 1
    if aa=='N':
        return 2
    if aa=='P':
        return 4
    if aa=='Q':
        return 2
    if aa=='R':
        return 6
    if aa=='S':
        return 6
    if aa=='T':
        return 4
    if aa=='V':
        return 4
    if aa=='W':
        return 1
    if aa=='Y':
        return 2
def mRNA_possibilities(protein):
    possibilities=3
    for i in range(0, len(protein), 1):
        possibilities=possibilities*redundancies(protein[i])
    return possibilities%1000000
protein=input()
print(mRNA_possibilities(protein))