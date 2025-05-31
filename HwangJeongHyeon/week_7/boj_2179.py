def fn(s1,s2):
    m=min(len(s1),len(s2))
    for i in range(m):
        if s1[i]!=s2[i]:
            return i
    return m

n=int(input())
s=[]
d=dict()
for i in range(n):
    s.append(input())
    d[s[i]]=i
s.sort()
m,ms1,ms2=-1,-1,-1

for i in range(n-1):
    for j in range(i+1,n):
        s1,s2=s[i],s[j]
        x = fn(s1,s2)
        #print(m,ms1,ms2,s1,s2)
        if m!=-1:
            if x<m:break
        if x==m and min(d[s1],d[s2])>d[ms1]:continue
        if x==m and min(d[s1],d[s2])==d[ms1] and max(d[s1],d[s2])>d[ms2]:continue
        m=x
        if d[s1]>d[s2]:
            ms1 = s2
            ms2 = s1
        else:
            ms1 = s1
            ms2 = s2
print(ms1)
print(ms2)
