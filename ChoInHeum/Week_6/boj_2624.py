import sys
input = sys.stdin.readline

T = int(input())
k = int(input())

coins = []
for _ in range(k):
    value, count = map(int, input().split())
    coins.append((value, count))

dp = [0] * (T + 1)
dp[0] = 1

for value, count in coins:
    temp = dp[:]
    for i in range(T + 1):
        for c in range(1, count + 1):
            if i - value * c < 0:
                break
            temp[i] += dp[i - value * c]
    dp = temp

print(dp[T])