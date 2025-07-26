T, W = map(int, input().split())
tree = [int(input()) for _ in range(T)]

dp = [[0] * (W + 1) for _ in range(T + 1)]

for t in range(1, T + 1):
    for w in range(W + 1):
        if w % 2 == 0:
            cur_pos = 1 
        else:
            cur_pos = 2

        if tree[t - 1] == cur_pos:
            if w == 0:
                dp[t][w] = dp[t-1][w] + 1
            else:
                dp[t][w] = max(dp[t-1][w], dp[t-1][w-1]) + 1
        else:
            if w == 0:
                dp[t][w] = dp[t-1][w]
            else:
                dp[t][w] = max(dp[t-1][w], dp[t-1][w-1])

print(max(dp[T]))