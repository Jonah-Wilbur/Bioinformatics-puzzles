import itertools
def listingValues(k):
    list=[]
    for i in range (1,k+1,1):
        list.append(i)
    for j in range (1,k+1,1):
        list.append(-1*j)
    return list
def signedPermutations(k):
    values = listingValues(k)
    permutations=list(itertools.permutations(values, k))
    permutations = [
        perm for perm in permutations
        if len(set(abs(x) for x in perm)) == len(perm)]
    return (len(permutations),permutations)
def cleaningPermutations(permut):
    permut=list(permut)
    for i in range(len(permut)):
        permut[i]=abs(permut[i])
    return(permut)
def printFunc(k):
    placeholder=signedPermutations(k)
    file.write(str(placeholder[0]))
    file.write("\n")
    for i in range(len(placeholder[1])):
        for j in range(len(placeholder[1][i])):
            file.write(str(placeholder[1][i][j]))
            file.write(' ')
        file.write("\n")
a=int(input())
file=open("SignedPermutationsOutput.txt", "w")
printFunc(a)