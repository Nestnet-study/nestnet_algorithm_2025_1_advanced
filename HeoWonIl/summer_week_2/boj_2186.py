import sys
input=sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m,k=map(int,input().rstrip().split())
graph=[list(input().rstrip()) for _ in range(n)]
target=input().rstrip()
d=[[[-1]*len(target) for _ in range(m)] for _ in range(n)]
ans=0

def dfs(x,y,p):
    global ans
    if p==len(target):
        return 1
    if d[x][y][p]!=-1:
        return d[x][y][p]

    d[x][y][p]=0

    for i in range(4):
        for j in range(1,k+1):
            nx=x+j*dx[i]
            ny=y+j*dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==target[p]:
                d[x][y][p]+=dfs(nx,ny,p+1)

    return d[x][y][p]

arr=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==target[0]:
            arr.append([i,j])
for [x,y] in arr:
    ans+=dfs(x,y,1)

print(ans)