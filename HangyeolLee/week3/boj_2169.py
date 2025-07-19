import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mars = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * M
dp[0] = mars[0][0]
for j in range(1, M):
    dp[j] = dp[j-1] + mars[0][j]

for i in range(1, N):
    left = [0] * M
    right = [0] * M

    left[0] = dp[0] + mars[i][0]
    for j in range(1, M):
        left[j] = max(dp[j], left[j-1]) + mars[i][j]

    right[M-1] = dp[M-1] + mars[i][M-1]
    for j in range(M-2, -1, -1):
        right[j] = max(dp[j], right[j+1]) + mars[i][j]

    for j in range(M):
        dp[j] = max(left[j], right[j])

print(dp[M-1])