
def FASTA_to_str(FASTA):
    string=''
    for i in range(len(FASTA)):
        if FASTA[i]!=' ':
            string=string+FASTA[i]
    return string
def motif_search(string, motif):
    output = []
    j=0
    for i in range(len(string)):
        if string[i]==motif[j]:
            output.append(i+1)
            j=j+1
        if j==len(motif):
            break
    if len(motif)==len(output):
        print(True)
    return output

string = FASTA_to_str(input())
motif = FASTA_to_str(input())
list=motif_search(string,motif)
for i in range(len(list)):
    print(list[i], end=' ')