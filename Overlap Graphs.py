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
            if prefix(DNA[j])==suffix(DNA[i]):
                print(index[i], index[j])
            if prefix(DNA[i])==suffix(DNA[j]):
                print(index[j], index[i])



strands=[]
names = []
input_data=input()
segments = input_data.split('>')
for segment in segments:
    if segment.strip():  # Ignore empty segments
        lines = segment.strip().split()
        name = lines[0]  # The first part is the name
        sequence = ''.join(lines[1:])  # Join the rest as the DNA sequence
        names.append(name)
        strands.append(FASTA_to_str(sequence))

print(names, strands)
overlap(names, strands)