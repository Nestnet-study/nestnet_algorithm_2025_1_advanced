'''
dp[r][c] : (0,0)부터 r,c까지의 합
dp[r][c]=dp[r-1][c]+dp[r][c+1]-dp[r-1][c-1]+met[r][c]
dp[-1][c]= dp[r][-1]=dp[-1][-1]=0

sum(r1,c1,r2,c2)(r1<=r2 and c1<=c2) = dp[r2][c2]-dp[r1-1][c2]-dp[r2][c1-1]+dp[r1-1][c1-1]
'''
def Sum(r1,c1,r2,c2):
    return dp[r1][c1]+dp[r2][c2]-dp[r2][c1]-dp[r1][c2]
n,m=map(int,input().split())
met=[[0]*(m+1)]
dp=[[0]*(m+1)]
for i in range(n):
    met.append([0]+list(map(int,input().split())))
    dp.append([0]*(m+1))
m+=1;n+=1

for i in range(1,n):
    for j in range(1,m):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+met[i][j]

#debug
'''
for i in range(n):
    for j in range(m):
        print("%5d"%dp[i][j],end=' ')
    print()
'''

mx=-10000*200*200
for r1 in range(n-1):
    for c1 in range(m-1):
        for r2 in range(r1+1,n):
            for c2 in range(c1+1,m):
                mx=max(mx,Sum(r1,c1,r2,c2))
print(mx)
