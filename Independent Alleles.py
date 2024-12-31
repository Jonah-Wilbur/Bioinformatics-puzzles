import math
def inverse_cumulative_binomial(n,p,k):
    sum=0
    for i in range(0,k):
        sum=sum+math.comb(n,i)*(p**i)*(1-p)**(n-i)
    return 1-sum

def situation(k,N):
    return round(inverse_cumulative_binomial(2**k,0.25,N),3)

k=int(input())
N=int(input())
print(situation(k,N))