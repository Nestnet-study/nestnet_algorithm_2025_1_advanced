# dp[i][j][k] i:몇번째, j는 위치(r,l), k는 움직인 횟수
# dp[i][j][k] = max(dp[i-1][j][k] , dp[i-1][not j][k-1]) #단 둘 중 하나 추가점수 +1점
# 1000*30*2
t,w=map(int,input().split())
a=[]
for i in range(t):
    a.append(int(input())-1) # [1 or 2]를 [0 or 1]로 저장
dp=[]
for i in range(t):
    dp.append([[0]*(w+1),[0]*(w+1)])
if a[0]==0:
    dp[0][0][0]=1
else:
    dp[0][1][1]=1
# bottom up
for i in range(t-1):
    for j in range(2):
        for k in range(w+1):
            if i==0 and j==1 and k==0:continue # 자두는 1번 자두나무 아래에 위치해 있다고 한다.
            if a[i+1]==j:
                dp[i+1][j][k]=max(dp[i+1][j][k],dp[i][j][k]+1)
                if k<w:dp[i+1][not j][k+1]=max(dp[i+1][not j][k+1],dp[i][j][k])
            else:
                dp[i+1][j][k]=max(dp[i+1][j][k],dp[i][j][k])
                if k<w:dp[i+1][not j][k+1]=max(dp[i+1][not j][k+1],dp[i][j][k]+1)
            
print(max(max(dp[t-1][0]),max(dp[t-1][1])))
