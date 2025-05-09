import sys
input = sys.stdin.readline

def move_cost(frm, to):
    if frm == to:
        return 1
    if frm == 0:
        return 2
    if abs(frm - to) == 2:
        return 4
    return 3

control = list(map(int, input().split()))
n = len(control) - 1 

INF = float('inf')
dp = [[[INF]*5 for _ in range(5)] for _ in range(n+1)]
dp[0][0][0] = 0  

for step in range(n):
    next_pos = control[step]
    for l in range(5):
        for r in range(5):
            if dp[step][l][r] != INF:
                dp[step+1][next_pos][r] = min(dp[step+1][next_pos][r],
                                              dp[step][l][r] + move_cost(l, next_pos))
                dp[step+1][l][next_pos] = min(dp[step+1][l][next_pos],
                                              dp[step][l][r] + move_cost(r, next_pos))

result = INF
for l in range(5):
    for r in range(5):
        result = min(result, dp[n][l][r])

print(result)
