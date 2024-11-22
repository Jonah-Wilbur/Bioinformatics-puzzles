def FASTA_to_str(FASTA):
    string=''
    for i in range(len(FASTA)):
        if FASTA[i]!=' ':
            string=string+FASTA[i]
    return string
def C(DNA):
    if DNA=='A':
        return ('T')
    if DNA=='T':
        return ('A')
    if DNA=='C':
        return ('G')    
    if DNA=='G':
        return('C')
def reverse_conjugate(strand):
    rev_conj=''
    for i in range(1, len(strand)+1, 1):
        rev_conj=rev_conj+C(strand[-i])
    return rev_conj
def restriction_sites(DNA):
    for i in range(0,len(DNA), 1):
        for j in range(4,13,1):
            if(DNA[i:i+j]==reverse_conjugate(DNA[i:i+j]) and i+j-1<len(DNA)):
                print(i+1, j)
    return 0

string = input()
restriction_sites(FASTA_to_str(string))