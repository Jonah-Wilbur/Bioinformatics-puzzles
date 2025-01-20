#introduction to Bioinformatics Armory
def countBases(DNA):
    return (DNA.count('A'), DNA.count('C'), DNA.count('G'),DNA.count('T'))
DNA=input()
output=[countBases(DNA)[0], countBases(DNA)[1], countBases(DNA)[2], countBases(DNA)[3]]
for o in output:
    print(o, end=' ')