import sys
input=sys.stdin.readline
from collections import deque

def air_bfs(i,j):
    q=deque()
    q.append([i,j])
    visited[i][j]=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==0 and real_graph[nx][ny]==0:
                    q.append([nx,ny])
                    visited[nx][ny]=1
                elif real_graph[nx][ny]==1:
                    visited[nx][ny]=visited[nx][ny]+1

n, m=map(int, input().split())
real_graph=[]
for i in range(n):
    real_graph.append(list(map(int, input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
time=0

while 1:
    visited=[[0 for _ in range(m)] for _ in range(n)]

    air_bfs(0,0)
    time+=1
	
    for i in range(n):
        for j in range(m):
            if visited[i][j]>=2:
                real_graph[i][j]=0

    block_cnt=0
    for i in range(n):
        for j in range(m):
            if real_graph[i][j]==0:
                block_cnt+=1
    if block_cnt==(n*m):
        break
    

print(time)