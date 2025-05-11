from collections import deque
def bfs(r,c):# r,c에서부터 가장 먼 거리를 반환하는 함수 (재귀x)
    d=((0,1),(0,-1),(1,0),(-1,0))
    dq=deque([[r,c,0]])
    a[r][c]=-1
    md=0
    while len(dq)>0:
        x,y,dist=dq.pop()
        md=max(md,dist)
        for d1,d2 in d:
            u,v=x+d1,y+d2
            if 0<=u and u<n and 0<=v and v<m and a[u][v]==1:
                a[u][v]=-1
                dq.appendleft((u,v,dist+1))
    dq=deque([[r,c]])
    a[r][c]=1
    while len(dq)>0:
        x,y=dq.pop()
        for d1,d2 in d:
            u,v=x+d1,y+d2
            if 0<=u and u<n and 0<=v and v<m and a[u][v]==-1:
                a[u][v]=1
                dq.appendleft((u,v))
    return md
                

n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(input()))
for i in range(n):
    for j in range(m):
        if a[i][j]=='L':
            a[i][j]=1
        else:
            a[i][j]=0
md=0
for i in range(n):
    for j in range(m):
        if a[i][j]==1:
            md=max(md,bfs(i,j))
print(md)
