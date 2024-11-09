def substring(s, t):
    vector=[]
    for i in range(0, len(s)-1, 1):
        if s[i:i+len(t)]==t:
            vector.append(str(i+1) + ' ')
    return ''.join(vector)


s = input()
t = input()
print(substring(s,t))