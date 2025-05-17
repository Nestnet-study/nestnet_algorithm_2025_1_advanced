import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
group = [[-1]*M for _ in range(N)]
group_size = dict()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

group_id = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and group[i][j] == -1:
            q = deque()
            q.append((i, j))
            group[i][j] = group_id
            cnt = 1

            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < M:
                        if graph[nx][ny] == 1 and group[nx][ny] == -1:
                            group[nx][ny] = group_id
                            q.append((nx, ny))
                            cnt += 1
            group_size[group_id] = cnt
            group_id += 1
            

result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            neighbor_groups = set()
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < N and 0 <= nj < M:
                    gid = group[ni][nj]
                    if gid != -1:
                        neighbor_groups.add(gid)
            total = 1
            for gid in neighbor_groups:
                total += group_size[gid]
            result = max(result, total)

print(result)
