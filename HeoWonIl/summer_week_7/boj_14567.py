from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
ind=[0]*(n+1)
ans=[0]*(n+1)
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().rstrip().split())
    graph[a].append(b)
    ind[b]+=1

q=deque()
for i in range(1,n+1):
    if ind[i]==0:
        q.append((i,1))
        ans[i]=1

while q:
    now,sem=q.popleft()
    for v in graph[now]:
        ind[v]-=1
        if ind[v]==0:
            q.append((v,sem+1))
            ans[v]=sem+1
            
print(' '.join(map(str,ans[1:])))