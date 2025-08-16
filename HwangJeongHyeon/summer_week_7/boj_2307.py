import sys
input = lambda : sys.stdin.readline().rstrip()
def fn(x=-1,y=-1):
    #print(x,y)
    visited=[0]*n
    b=[]
    for i in range(n):
        b.append([inf]*n)
        b[i][i]=0
    c=[inf]*n
    c[0]=0
    #
    for _ in range(n):
        mn=-1
        for i in range(n):
            if visited[i]:continue
            if mn==-1 or c[mn]>c[i]:
                mn=i
        visited[mn]=1
        for i,j in a[mn]:
            if (mn==x and i==y) or (mn==y and i==x):
                #print(mn,i,j)
                continue
            c[i]=min(c[i],c[mn]+j)
    if x==-1 and y==-1: # 역추적
        visited=[0]*n
        stack=[n-1]
        while len(stack):
            last=stack.pop(-1)
            if visited[last]:continue
            visited[last]=1
            for before,t in a[last]:
                if c[before]+t==c[last]:
                    stack.append(before)
                    d.append([last,before])
    return c[-1]
n,m=map(int,input().split())
a=[]
d=[]
inf = 2**31-1
for i in range(n):
    a.append([])
for i in range(m):
    x,y,t=map(int,input().split())
    x-=1;y-=1
    a[x].append([y,t])
    a[y].append([x,t])

g=fn()

k=0
for x,y in d:
    if x>y:x,y=y,x
    k=max(fn(x,y),k)
    if k==inf:break
if k==inf:
    print(-1)
else:
    print(k-g)

