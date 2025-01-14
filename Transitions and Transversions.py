#Transition: A-G or C-T
#Transversion: Any other point mutation
def FASTA_to_str(FASTA):
    string=''
    for i in range(len(FASTA)):
        if FASTA[i]!=' ':
            string=string+FASTA[i]
    return string

def transition(char1, char2):
    if char1=='T' and char2=='C':
        return True
    elif char1=='C' and char2=='T':
        return True
    elif char1=='A' and char2=='G':
        return True
    elif char1=='G' and char2=='A':
        return True
    else:
        return False
    

def t_t_ratio(Sequence1, Sequence2):
    transition_count=0
    transversion_count=0
    for i in range(len(Sequence1)):
        if Sequence1[i]==Sequence2[i]:
            continue
        elif transition(Sequence1[i],Sequence2[i])==True:
            transition_count=transition_count+1
        else:
            transversion_count=transversion_count+1
    return transition_count/transversion_count

S1=input()
S2=input()
print(t_t_ratio(S1,S2))