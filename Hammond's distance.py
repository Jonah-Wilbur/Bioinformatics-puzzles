import numpy as np

s = str(input())
t = str(input())
H=0
for i in range(len(s)):
    if s[i]!=t[i]:
        H=H+1
print(H)