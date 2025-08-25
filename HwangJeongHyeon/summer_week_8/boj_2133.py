dp=[0]*31
dp[0]=1
dp[2]=3
n=int(input())
for i in range(4,31,2):
    dp[i]=dp[i-2]*dp[2]
    for j in range(i-4,-2,-2):
        dp[i]+=dp[j]*2
print(dp[n])
