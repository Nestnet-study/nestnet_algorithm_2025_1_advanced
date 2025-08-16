n,m = map(int, input().split())

lect = [[] for _ in range(n+1)]
dp = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())

    lect[b].append(a)

dp[1] = 1
for i in range(2, n+1):
    if not lect[i]:
        dp[i] = 1
    else:
        m = 1
        for j in range(len(lect[i])):
            if dp[lect[i][j]] > m:
                m = dp[lect[i][j]]
        
        dp[i] = m+1

for i in range(1,n+1):
    print(dp[i], end=" ")
    