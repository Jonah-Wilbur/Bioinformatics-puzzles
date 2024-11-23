import math
def FASTA_to_str(FASTA):
    string=''
    for i in range(len(FASTA)):
        if FASTA[i]!=' ':
            string=string+FASTA[i]
    return string
def probability_match(DNA, GC):
    p_AT = (1-GC)/2
    p_GC = GC/2
    total_prob = 1
    return math.log10((p_AT**DNA.count('A'))*(p_AT**DNA.count('T'))*(p_GC**DNA.count('C'))*(p_GC**DNA.count('G')))

def loop(DNA, array):
    answer=[]
    for i in range(len(array)):
        answer.append(probability_match(DNA,array[i]))
    return answer

def nice_output(array):
    string = ''
    for i in range(len(array)):
        string=string+str(round((array[i]),3))+' '
    return string

strand=input()
array = [float(item) for item in input().split()]

print(nice_output((loop(FASTA_to_str(strand), array))))