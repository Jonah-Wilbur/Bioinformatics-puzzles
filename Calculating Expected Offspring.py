def expected_dominant_phenotype(array):
    return 2*array[0] + 2*array[1] + 2*array[2] + 3*array[3]/2 + array[4]
arr=[]
for i in range (0,6,1):
    arr.append(int(input()))
print(expected_dominant_phenotype(arr)) #absurdly easy question