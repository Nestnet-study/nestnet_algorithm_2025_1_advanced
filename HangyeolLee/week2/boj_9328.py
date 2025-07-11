import sys
from collections import deque
input = sys.stdin.readline

t = int(input()) # 테스트 케이스
way = [[1,0], [0,1], [-1,0], [0,-1]]

for _ in range(t):
    h, w = map(int, input().split())

    build = [0] * h
    for i in range(h):
        build[i] = list(input())
    
    key = input().rstrip()

    visited = [[0] * w for _ in range(h)]

    alpha = [[] for _ in range(26)]
    keys = [0] * 26

    if key != '0':
        for i in key:
            keys[ord(i)-97] = 1

    # 1) 시작 큐에 넣을 때도 visited 처리
    queue = deque()
    # 상·하단 행
    for j in range(w):
        if build[0][j] != '*':
            visited[0][j] = 1; queue.append((0, j))
        if build[h-1][j] != '*':
            visited[h-1][j] = 1; queue.append((h-1, j))
    # 좌·우단 열 (코너는 이미 처리됐으므로 1..h-2)
    for i in range(1, h-1):
        if build[i][0] != '*':
            visited[i][0] = 1; queue.append((i, 0))
        if build[i][w-1] != '*':
            visited[i][w-1] = 1; queue.append((i, w-1))


    answer = 0
    while queue:
        x, y = queue.popleft()
        cell = build[x][y]

        if cell.isalpha():
            # 2) 문(대문자)
            if cell.isupper():
                idx = ord(cell) - 65
                if keys[idx]:
                    # 열쇠가 있으면 인접 enqueue & visited 처리
                    for dx, dy in way:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and build[nx][ny] != '*':
                            visited[nx][ny] = 1
                            queue.append((nx, ny))
                else:
                    alpha[idx].append((x, y))

            # 3) 열쇠(소문자)
            else:
                idx = ord(cell) - 97
                if keys[idx] == 0:
                    keys[idx] = 1
                    # 잠겨 있던 문들 즉시 풀기 (enqueue 앞쪽으로)
                    for px, py in alpha[idx]:
                        for dx, dy in way:
                            nx, ny = px+dx, py+dy
                            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and build[nx][ny] != '*':
                                visited[nx][ny] = 1
                                queue.append((nx, ny))
                    alpha[idx].clear()
                # 현재 열쇠 칸 주변 이동
                for dx, dy in way:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and build[nx][ny] != '*':
                        visited[nx][ny] = 1
                        queue.append((nx, ny))

        # 4) 빈칸(.) 또는 보물($)
        elif cell == '.' or cell == '$':
            if cell == '$':
                answer += 1
            for dx, dy in way:
                nx, ny = x+dx, y+dy
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and build[nx][ny] != '*':
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

    print(answer)