import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

miro = [[0] * n for _ in range(n)] # 미로
min_count = [[-1] * n for _ in range(n)] # 검-흰 바꾼 최소 횟수

for i in range(n):
    miro[i] = list(map(int, input().rstrip()))

way = [[1,0], [0,1], [-1,0], [0,-1]] # 네 방향으로 가는 것
answer = -1 # 정답

def bfs():
    global answer
    
    queue = deque()
    queue.append((0,0,0)) # 시작점 큐에 넣기; 값 설명 -> (열 좌표, 행 좌표, 방 바꾼 횟수)

    while(queue):
        cur = queue.popleft()

        if cur[0] == n-1 and cur[1] == n-1: # 도착했는지 판단
            if answer == -1 or answer > cur[2]:
                answer = cur[2]
            continue

        if 0 <= cur[0] < n and 0 <= cur[1] < n: # 미로를 벗어나는지 판단
            if min_count[cur[0]][cur[1]] == -1 or min_count[cur[0]][cur[1]] > cur[2]: # 검-흰 바꾼 최소 횟수보다 작으면 진행
                min_count[cur[0]][cur[1]] = cur[2]
            else: # 횟수보다 크면 continue
                continue

            if miro[cur[0]][cur[1]] == 0: # 검은방이면 + 1 
                for i in way:
                    queue.append((cur[0]+i[0], cur[1]+i[1], cur[2]+1))
            else:
                for i in way:
                    queue.append((cur[0]+i[0],cur[1]+i[1],cur[2]))

bfs()

print(answer)