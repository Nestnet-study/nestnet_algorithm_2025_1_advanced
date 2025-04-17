from math import sqrt
from collections import deque
from heapq import *
def dfs(x):
    global countdown
    visited[x]=1;
    countdown-=1
    for i in range(n):
        if visited[i]==0:
            heappush(hq, (dist((a[x][0],a[x][1]),(a[i][0],a[i][1])),x,i))
    if x in g.keys():
        for i in g[x]:
            if visited[i]==0:
                dfs(i)
def dist(a,b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


n,m=map(int,input().split())
a=[]

for i in range(n):
    a.append(list(map(int,input().split())))

g=dict()# 1: [1, 2 ,3]

for i in range(m):
    p,q=map(int,input().split())
    p-=1;q-=1;
    if not p in g.keys():
        g[p]=[]
    if not q in g.keys():
        g[q]=[]
    g[p].append(q)
    g[q].append(p)
visited=[0]*1000
visited[0]=1

hq=[]
countdown=n
dfs(0)

s=0
while hq!=[] and countdown>0:
    r,x,y = heappop(hq)
    if visited[x] and visited[y]:
        continue;
    if visited[x]:
        dfs(y)
    else:
        dfs(x)
    
    s+=r
print("%.2f"%(s))
"""
1번에서 그래프 탐색하며 모든 정점에서 다른 정점으로 갈 수 있는 통로의 길이를 저장
가장 작은 길이의 통로가 이미 방문하지 않았다면, 방문하고 그래프 탐색
모든 정점을 탐색하면 종료.
"""
