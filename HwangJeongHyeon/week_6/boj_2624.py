'''
   0                   1                   2
   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
0  1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
10 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1
5  1 0 0 0 0 1 0 0 0 0 2 0 0 0 0 2 0 0 0 0 2
1  1 1 1 1 1 2 1 1 1 1 3 2 2 2 2 4 2 2 2 2 4
'''

t=int(input())
k=int(input())
a=[]
for i in range(k):
    a.append(list(map(int,input().split())))
a.sort(reverse = True)

dp=[[0]*(t+1)]
dp[0][0]=1
for i in range(k):
    dp.append([0]*(t+1))

for i in range(k):
    for j in range(t+1):
        if dp[i][j]!=0:
            for u in range(1+a[i][1]):
                if j+u*a[i][0]>t:break
                dp[i+1][j+u*a[i][0]]+=dp[i][j]
print(dp[k][t])
