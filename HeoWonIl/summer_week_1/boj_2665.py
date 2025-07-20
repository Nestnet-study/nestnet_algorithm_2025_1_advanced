import heapq as hq
import sys
input=sys.stdin.readline

INF=int(10e9)
dx=[-1,0,1,0]
dy=[0,1,0,-1]

n=int(input())
graph=[list(map(int,list(input().rstrip()))) for _ in range(n)]
d=[[INF]*n for _ in range(n)]

def dijkstra(sx,sy):
    q = []
    hq.heappush(q, (0, sx, sy))
    d[sx][sy]=0

    while q:
        dist,x,y=hq.heappop(q)
        if x==n-1 and y==n-1:
            print(d[n-1][n-1])
            break
        # 이미 더 짧은 경로가 발견된 경우
        if d[x][y]<dist:
            continue

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                # 이동 비용 계산
                # 1은 벽이 없으므로 비용이 0, 0은 벽이 있으므로 비용이 1
                cost=dist+(not graph[nx][ny])
                if cost<d[nx][ny]:
                    d[nx][ny]=cost
                    hq.heappush(q,(cost,nx,ny))

dijkstra(0,0)