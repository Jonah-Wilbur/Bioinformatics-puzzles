def probability_match(DNA, GC):
    p_AT = (1-GC)/2
    p_GC = GC/2
    return (p_AT**DNA.count('A'))*(p_AT**DNA.count('T'))*(p_GC**DNA.count('C'))*(p_GC**DNA.count('G'))

def expected_restriction_sites(Seq,x,N):
    return (N-len(Seq)+1)*probability_match(Seq,x)

def actual_function(Array,Sequence,N):
    answers=[]
    for i in range(len(Array)):
        answers.append(expected_restriction_sites(Sequence,Array[i],N))
    return answers

def nice_output(Array):
    string = ''
    for i in range(len(Array)):
        string=string+str(round((Array[i]),4))+' '
    return string

N=int(input())
Seq=input()
array = [float(item) for item in input().split()]
print(nice_output(actual_function(array,Seq,N)))