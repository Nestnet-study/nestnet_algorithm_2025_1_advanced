import sys
input = sys.stdin.readline

N,M,K = map(int, input().split())
words = [list(input().rstrip()) for _ in range(N)]
word  = input().rstrip()
start = [(i,j) for i in range(N) for j in range(M) if words[i][j] == word[0]]
way   = [(0,1),(0,-1),(1,0),(-1,0)]

answer = 0
L = len(word)
# check[n][x][y]: word[n:]를 (x,y)에서 완성할 경로 수
check = [[[-1]*M for _ in range(N)] for _ in range(L)]

def dfs(x, y, n):
    if words[x][y] != word[n]:
         return 0
    if n == L-1:
         return 1
    if check[n][x][y] != -1:
         return check[n][x][y]

    total = 0
    # 1칸부터 K칸까지 상·하·좌·우 이동
    for dx, dy in way:
        for step in range(1, K+1):
            nx, ny = x + dx*step, y + dy*step
            if 0 <= nx < N and 0 <= ny < M:
                total += dfs(nx, ny, n+1)

    check[n][x][y] = total
    return total

for i, j in start:
    answer += dfs(i, j, 0)

print(answer)