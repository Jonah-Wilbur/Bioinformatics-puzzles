def printlist(list):
    for i in range(len(list)):
        print(list[i], end=' ')
def C(DNA):
    limit=len(DNA)
    Complement=''
    for i in range (limit):
        if DNA[i]=='A':
            Complement=Complement+'T'
        if DNA[i]=='T':
            Complement=Complement+'A'
        if DNA[i]=='C':
            Complement=Complement+'G'    
        if DNA[i]=='G':
            Complement=Complement+'C'
    return Complement
def R(str):
    limit=len(str)
    Reverse=''
    i=1
    for i in range(limit+1):
        Reverse=Reverse+str[-i]
    return Reverse[1:]
def Reverse_Complement(DNA):
    cDNA=C(DNA)
    rDNA=R(cDNA)
    return rDNA
def FASTA_to_str(FASTA):
    string=''
    for i in range(len(FASTA)):
        if FASTA[i]!=' ':
            string=string+FASTA[i]
    return string
def DNA_to_RNA(DNA):
    RNA=''
    for i in range(len(DNA)):
        if DNA[i]=='T':
            RNA=RNA+'U'
        else:
            RNA=RNA+DNA[i]
    return RNA
def AA(RNA):
    if RNA=='GCC' or RNA=='GCU' or RNA=='GCA' or RNA=='GCG':
        return 'A'
    if RNA=='UGU' or RNA=='UGC':
        return 'C'
    if RNA=='GAU' or RNA=='GAC':
        return 'D'
    if RNA=='GAA' or RNA=='GAG':
        return 'E'
    if RNA=='UUU' or RNA=='UUC':
        return 'F'
    if RNA=='GGU' or RNA=='GGC' or RNA=='GGA' or RNA=='GGG':
        return 'G'
    if RNA=='CAU' or RNA=='CAC':
        return 'H'
    if RNA=='AUU' or RNA=='AUC' or RNA=='AUA':
        return 'I'
    if RNA=='AAA' or RNA=='AAG':
        return 'K'
    if RNA=='UUA' or RNA=='UUG' or RNA=='CUU' or RNA=='CUC' or RNA=='CUA' or RNA=='CUG':
        return 'L'
    if RNA=='AUG':
        return 'M'
    if RNA=='AAU' or RNA=='AAC':
        return 'N'
    if RNA=='CCU' or RNA=='CCC' or RNA=='CCA' or RNA=='CCG':
        return 'P'
    if RNA=='CAA' or RNA=='CAG':
        return 'Q'
    if RNA=='CGU' or RNA=='CGC' or RNA=='CGA' or RNA=='CGG' or RNA=='AGA' or RNA=='AGG':
        return 'R'
    if RNA=='UCU' or RNA=='UCC' or RNA=='UCA' or RNA=='UCG' or RNA=='AGU' or RNA=='AGC' :
        return 'S'
    if RNA=='ACU' or RNA=='ACC' or RNA=='ACA' or RNA=='ACG':
        return 'T'
    if RNA=='GUU' or RNA=='GUC' or RNA=='GUA' or RNA=='GUG':
        return 'V'
    if RNA=='UGG':
        return 'W'
    if RNA=='UAU' or RNA=='UAC':
        return 'Y'
    if RNA=='UAA' or RNA=='UAG' or RNA=='UGA':
        return ' '
    else:
        return '  ERROR  '
def RNA_to_Codons(RNA):
    Codons = [RNA[i:i+3] for i in range(0, len(RNA), 3)]
    if len(Codons[-1])!=3:
        Codons.pop()
    return Codons
def translation(Seq):
    Protein=[]
    for i in range(len(Seq)):
        Protein.append(AA(Seq[i]))
        if AA(Seq[i])==' ':
            break
    return ''.join(Protein)
def translation_from_any_point(DNA):
    RNA=DNA_to_RNA(DNA)
    Codons=RNA_to_Codons(RNA)
    return translation(Codons)
def translation_from_all_points(DNA):
    proteins=[]
    for i in range(0,len(DNA),1):
        if DNA[i:i+3]=='ATG':
            for j in range(i,len(DNA),3):
                if DNA[j:j+3]=='TAA' or DNA[j:j+3]=='TAG' or DNA[j:j+3]=='TGA':
                    proteins.append(translation_from_any_point(DNA[i:j+3]))
                    break
    #add something to account for the reverse complement
    rDNA=Reverse_Complement(DNA)
    for i in range(0,len(rDNA),1):
        if rDNA[i:i+3]=='ATG':
            for j in range(i,len(rDNA),3):
                if rDNA[j:j+3]=='TAA' or rDNA[j:j+3]=='TAG' or rDNA[j:j+3]=='TGA':
                    proteins.append(translation_from_any_point(rDNA[i:j+3]))
                    break
    proteins= list(dict.fromkeys(proteins))
    return proteins

DNA=FASTA_to_str(input())
printlist(translation_from_all_points(DNA))