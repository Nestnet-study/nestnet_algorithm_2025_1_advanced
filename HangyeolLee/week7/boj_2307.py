import sys
import heapq

input = sys.stdin.readline
INF = 10**18

def dijkstra(n, graph, ban=None):
    dist = [INF] * (n + 1)
    prev = [-1] * (n + 1)  # 경로 복원용
    dist[1] = 0
    pq = [(0, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        if u == n:  # N까지 최단 도달 시 조기 종료(선택)
            break
        for v, w in graph[u]:
            if ban and ((u == ban[0] and v == ban[1]) or (u == ban[1] and v == ban[0])):
                continue
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, prev

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))


dist0, prev = dijkstra(N, graph)
if dist0[N] == INF:
    print(-1)  # 애초에 1→N 불가능
    exit()

edges_on_path = []
cur = N
while prev[cur] != -1:
    p = prev[cur]
    edges_on_path.append((p, cur))
    cur = p

base = dist0[N]
ans = 0
for e in edges_on_path:
    dist_ban, _ = dijkstra(N, graph, ban=e)
    if dist_ban[N] == INF:
        print(-1)  # 이 간선 막으면 도달 불가 → 지연 무한대
        exit()
    ans = max(ans, dist_ban[N] - base)
print(ans)