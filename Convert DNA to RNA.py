import numpy as np

DNA=input()
limit=len(DNA)
A='A'
T='T'
U='U'
C='C'
G='G'
RNA=''
i = 0
for i in range (limit):
    if DNA[i]=='A':
        RNA=RNA+A
    if DNA[i]==T:
        RNA=RNA+U
    if DNA[i]==C:
        RNA=RNA+C
    if DNA[i]==G:
        RNA=RNA+G
print(RNA)