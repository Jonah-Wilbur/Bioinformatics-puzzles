def AA(RNA):
    if RNA=='GCC' or RNA=='GCU' or RNA=='GCC' or RNA=='GCG':
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
def RNA_to_Codons(RNA):
    Codons = [RNA[i:i+3] for i in range(0, len(RNA), 3)]
    return Codons


Sequence=str(input())
def translation(Seq):
    Protein=[]
    for i in range(len(Seq)):
        Protein.append(AA(Seq[i]))
    return ''.join(Protein)
print(translation(RNA_to_Codons(Sequence)))