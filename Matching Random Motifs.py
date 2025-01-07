#for a string of length A with GC content X there are how many possible ways to do it?
#Can have permutations of two classes of characters
#Permutations of A and B goes to AABB, ABAB, BBAA, etc
#N!/((1-x)*N!*(xN)!)*2^N
import math

def probability_match(DNA, GC):
    p_AT = (1-GC)/2
    p_GC = GC/2
    total_prob = 1
    return (p_AT**DNA.count('A'))*(p_AT**DNA.count('T'))*(p_GC**DNA.count('C'))*(p_GC**DNA.count('G'))

def prob(N, x, sequence):
    #binomial?
    p_0=(1-probability_match(sequence, x))**N
    return round(1-p_0,3)

N=int(input())
x=float(input())
sequence=input()
print(prob(N,x,sequence))