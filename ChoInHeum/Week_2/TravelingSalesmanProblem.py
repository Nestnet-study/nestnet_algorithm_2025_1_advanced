import sys

INF = float('inf')

def tsp(N, W):
    dp = [[INF] * N for _ in range(1 << N)]
    dp[1][0] = 0

    for mask in range(1 << N):
        for u in range(N):
            if mask & (1 << u):
                for v in range(N):
                    if not (mask & (1 << v)) and W[u][v] != 0:
                        new_mask = mask | (1 << v)
                        dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + W[u][v])
    
    result = INF
    for i in range(1, N):
        if W[i][0] != 0:
            result = min(result, dp[(1 << N) - 1][i] + W[i][0])
    
    return result

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

print(tsp(N, W))
