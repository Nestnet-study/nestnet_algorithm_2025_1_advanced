import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    dp[i] = [0] * 21

dp[0][arr[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        if dp[i-1][j] != 0: # 가능한 수들만 진행
            if 0 <= j-arr[i]: # 음수가 안되면
                dp[i][j-arr[i]] += dp[i-1][j]

            if j+arr[i] <= 20: # 20넘는 수가 안되면
                dp[i][j+arr[i]] += dp[i-1][j]

print(dp[n-2][arr[-1]])