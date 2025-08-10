import sys
input = sys.stdin.readline

n = int(input())
train = list(map(int, input().split()))
l = int(input())

rsum = [0] * (n+1)
for i in range(1, n+1):
    rsum[i] = rsum[i-1] + train[i-1]

dp = [[0] * (n+1) for _ in range(4)] 

for k in range(1, 4):
    for i in range(k*l, n+1): 
        dp[k][i] = max(dp[k][i-1], dp[k-1][i-l] + (rsum[i] - rsum[i-l]))

print(dp[3][n])