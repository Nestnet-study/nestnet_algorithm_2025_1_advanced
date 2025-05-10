from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy, grid, h, w):
    visited = [[-1]*w for _ in range(h)]
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = 0

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < h and 0 <= ny < w:
                if grid[nx][ny] != 'x' and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return visited

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    grid = []
    positions = []
    for i in range(h):
        row = list(input().strip())
        for j in range(w):
            if row[j] == 'o':
                start = (i, j)
            elif row[j] == '*':
                positions.append((i, j))
        grid.append(row)

    positions = [start] + positions
    n = len(positions)
    dist = [[-1]*n for _ in range(n)]
    possible = True

    for i in range(n):
        bfs_result = bfs(positions[i][0], positions[i][1], grid, h, w)
        for j in range(n):
            dist[i][j] = bfs_result[positions[j][0]][positions[j][1]]
            if dist[i][j] == -1:
                possible = False

    if not possible:
        print(-1)
        continue

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dfs(pos, visited):
        if visited == (1 << n) - 1:
            return 0
        res = float('inf')
        for next in range(1, n):
            if not visited & (1 << next):
                d = dist[pos][next]
                if d != -1:
                    res = min(res, dfs(next, visited | (1 << next)) + d)
        return res

    result = dfs(0, 1)
    print(result if result != float('inf') else -1)
