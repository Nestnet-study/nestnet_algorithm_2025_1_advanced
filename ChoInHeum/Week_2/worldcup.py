from itertools import combinations as cb
from sys import stdin

def dfs(depth):
    global cnt
    
    if depth == 15:
        cnt = 1
        for sub in res:
            if sub.count(0) != 3:
                cnt = 0
                break
        return
    t1, t2 = game[depth]
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if res[t1][x] > 0 and res[t2][y] > 0:
            res[t1][x] -= 1
            res[t2][y] -= 1
            dfs(depth + 1)
            res[t1][x] += 1
            res[t2][y] += 1

answer = []
game = list(cb(range(6), 2))

for _ in range(4):
    data = list(map(int, stdin.readline().split()))
    res = [data[i:i+3] for i in range(0, 18, 3)]
    cnt = 0
    dfs(0)
    answer.append(cnt)
    
print(*answer)