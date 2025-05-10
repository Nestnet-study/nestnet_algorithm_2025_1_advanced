from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y, grid, h, w):
    visited = [[-1] * w for _ in range(h)]
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 'L' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                
    return visited

def find_max_distance(grid, h, w):
    max_dist = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'L':
                visited = bfs(i, j, grid, h, w)
                for row in visited:
                    max_dist = max(max_dist, max(row))
    return max_dist

h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]

print(find_max_distance(grid, h, w))
