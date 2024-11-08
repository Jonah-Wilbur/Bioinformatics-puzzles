from math import comb
k = int(input()) # number of homozygous dominant individuals
m = int(input()) # number of heterozygous individuals
n = int(input()) # number of homozygous recessive individuals

print((comb(k,2) + k*m + k*n + 0.5*m*n + 0.75*comb(m,2))/(comb(k+m+n,2))) # probability of one offspring, produced by any pair, of having the dominant phenotype