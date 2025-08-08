import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

rx_init, ry_init, bx_init, by_init = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx_init, ry_init = i, j
        elif board[i][j] == 'B':
            bx_init, by_init = i, j

def slide(x, y, dx, dy):
    count = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

q = deque()
q.append((rx_init, ry_init, bx_init, by_init, 0))
visited = set()
visited.add((rx_init, ry_init, bx_init, by_init))

while q:
    rx, ry, bx, by, depth = q.popleft()

    if depth >= 10:
        continue

    nrx, nry, r_count = slide(rx, ry, -1, 0)
    nbx, nby, b_count = slide(bx, by, -1, 0)

    if board[nbx][nby] != 'O':
        if board[nrx][nry] == 'O':
            print(depth + 1)
            exit(0)
        
        if nrx == nbx and nry == nby:
            if r_count > b_count: nrx += 1
            else:                 nbx += 1
        
        if (nrx, nry, nbx, nby) not in visited:
            visited.add((nrx, nry, nbx, nby))
            q.append((nrx, nry, nbx, nby, depth + 1))


    nrx, nry, r_count = slide(rx, ry, 1, 0)
    nbx, nby, b_count = slide(bx, by, 1, 0)
    
    if board[nbx][nby] != 'O':
        if board[nrx][nry] == 'O':
            print(depth + 1)
            exit(0)
            
        if nrx == nbx and nry == nby:
            if r_count > b_count: nrx -= 1
            else:                 nbx -= 1
            
        if (nrx, nry, nbx, nby) not in visited:
            visited.add((nrx, nry, nbx, nby))
            q.append((nrx, nry, nbx, nby, depth + 1))


    nrx, nry, r_count = slide(rx, ry, 0, -1)
    nbx, nby, b_count = slide(bx, by, 0, -1)

    if board[nbx][nby] != 'O':
        if board[nrx][nry] == 'O':
            print(depth + 1)
            exit(0)
            
        if nrx == nbx and nry == nby:
            if r_count > b_count: nry += 1
            else:                 nby += 1

        if (nrx, nry, nbx, nby) not in visited:
            visited.add((nrx, nry, nbx, nby))
            q.append((nrx, nry, nbx, nby, depth + 1))


    nrx, nry, r_count = slide(rx, ry, 0, 1)
    nbx, nby, b_count = slide(bx, by, 0, 1)

    if board[nbx][nby] != 'O':
        if board[nrx][nry] == 'O':
            print(depth + 1)
            exit(0)
            
        if nrx == nbx and nry == nby:
            if r_count > b_count: nry -= 1
            else:                 nby -= 1

        if (nrx, nry, nbx, nby) not in visited:
            visited.add((nrx, nry, nbx, nby))
            q.append((nrx, nry, nbx, nby, depth + 1))

print(-1)