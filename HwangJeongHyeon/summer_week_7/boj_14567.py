# 위상정렬
import sys
input=lambda : sys.stdin.readline().rstrip()
n,m=map(int,input().split())
a=[0]*n
b=[]
for i in range(n):
    b.append([])
for i in range(m):
    x,y=map(int,input().split())
    x-=1;y-=1
    b[x].append(y)
    a[y]+=1
count=0
c=[]
d=[0]*n
while True:
    count+=1
    c=[]
    for i in range(n):
        if a[i]==0:
            c.append(i)
    for i in c:
        for j in b[i]:
            a[j]-=1
        d[i]=count
        a[i]=-1
    if c==[]:
        break
for i in range(n):
    print(d[i],end=' ')
