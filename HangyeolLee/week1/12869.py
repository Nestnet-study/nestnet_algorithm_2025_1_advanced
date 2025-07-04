import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

n = int(input())
inp_scv = list(map(int, input().split()))

# SCV가 3마리 미만일 때는 0으로 패딩
scv = inp_scv + [0] * (3 - n)

damage = [9, 3, 1]
damage_way = list(permutations(damage))

# 최대 체력 60이므로 0~60
HP = 60
visited = [[[False] * (HP + 1) for _ in range(HP + 1)] for _ in range(HP + 1)]

def bfs():
    queue = deque()
    # (hp1, hp2, hp3, cnt)
    queue.append((scv[0], scv[1], scv[2], 0))
    visited[scv[0]][scv[1]][scv[2]] = True

    while queue:
        a, b, c, cnt = queue.popleft()
        # 다 잡았으면
        if a <= 0 and b <= 0 and c <= 0:
            print(cnt)
            return

        for d1, d2, d3 in damage_way:
            na = max(0, a - d1)
            nb = max(0, b - d2)
            nc = max(0, c - d3)
            if not visited[na][nb][nc]:
                visited[na][nb][nc] = True
                queue.append((na, nb, nc, cnt + 1))

bfs()