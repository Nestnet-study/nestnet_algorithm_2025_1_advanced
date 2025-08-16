import sys
input=sys.stdin.readline
import heapq as hq

INF=int(10e9)
n,m=map(int,input().rstrip().split())
graph=[[] for _ in range(n+1)]

roads=[]
for _ in range(m):
    a,b,dist=map(int,input().rstrip().split())
    graph[a].append([b,dist])
    graph[b].append([a,dist])
    roads.append((a,b))

def dijkstra(s,a,b):
    dis=[INF]*(n+1)
    q=[]
    hq.heappush(q,(0,s))
    dis[s]=0

    while q:
        dis_acc,x=hq.heappop(q)

        if dis[x]<dis_acc:
            continue

        for y,dist in graph[x]:
            # 핵심 아이디어: 검문하고 있는 곳은 pass!
            if (x==a and y==b) or (x==b and y==a):
                continue
            dist_sum=dis_acc+dist
            if dist_sum<dis[y]:
                dis[y]=dist_sum
                hq.heappush(q,(dist_sum,y))
    if dis[n]==INF:
        return -1
    return dis[n]

ans=0
min_t=0
# 검문 x
min_t=dijkstra(1,0,0)
# 각 도로마다 검문 수행
for i,j in roads:
    t=dijkstra(1,i,j)
    if t==-1:
        ans=-1
        break
    else:
        ans=max(ans,t-min_t)
print(ans)




