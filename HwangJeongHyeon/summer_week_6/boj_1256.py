'''
a : 1, z : 0
a
a : 0, z : 1
z
a : 1, z : 1
az
za
a : 3, z : 4
만약 작으면 둘다 -1 -1
크면 -1 0
5 3
------- 4 2
aaazz   3 1
aazaz
aazza

azaaz   2 1
azaza

azzaa   1 1
------- 3 2
zaaaz   2 1
zaaza

zazaa   1 1
------- 2 2
zzaaa   1 1

dp
  0 1 2 3 4 5 j
0 1
1 1 1
2 1 2 1
3 1 3 3 1
4 1 4 6 4 1
5 1 5 10105 1
i

dp[i][j] = dp[i-1][j-1] + ... + dp[j-1][j-1]
dp[i][1] : i+1
# 1 첫번째a가 0위치에 있는지 확인 즉 a가 0위치에 있는 모든 경우의 수보다 더 크면 첫번째 a는
#   0위치에 없음 1위치에 있는지 확인
# 2 만약 해당 위치에 있으면 두번째 a를 확인
dp[i][j] 개수 i개중 a가 j개 있음을 뜻함.
dp[i][j] = dp[i][j]
dp[n+m][n]
크면 -1
작으면 dp[n+m][n]
'''
n,m,k=map(int,input().split())
a,b=n+m,n
dp=[]
res=['z']*a
x=[]
for i in range(a+1):
    dp.append([])
    for j in range(min(b+1,i+1)):
        if j==0 or i==j:
            dp[i].append(1)
        else:
            dp[i].append(dp[i-1][j]+dp[i-1][j-1])
while True:
    #input("all:%d a:%d 남은:%d dp:%d"%(a,b,k,dp[a][b]))
    if dp[a][b]<k: # 크면
        if a==n+m:
            print(-1)
            exit()
        k-=dp[a][b]
        a-=1;
        
    elif dp[a][b]>=k and b>=0: # 작으면
        #print(n+m-a-1)
        if n+m-a-1!=-1:
            x.append(n+m-a-1)
        a-=1;b-=1
    else:break

        


for i in range(n):
    res[x[i]]='a'
print(str(res).replace('[','').replace(']','').replace(',','').replace(' ','').replace('\'',''))











