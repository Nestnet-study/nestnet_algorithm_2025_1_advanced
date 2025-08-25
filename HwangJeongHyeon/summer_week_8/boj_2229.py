'''
[2 5] [7 1] [3 4 8 6] [9 3]
그리디 안됨
3 9 1 4



2 5 7 1 3 4 8 6 9 3

2 5 7 1 3 4  8  6  9  3]
0 3 5 9 9 10 14 14 17 20

dp[i] : i번째까지 고려했을 때 최대 점수
dp[i] = max(score(i-j,i)+dp[i-j-1])

4 6 3 5 4 3 7 5 1 3 2 5 6 4 6 5 7

'''
n=int(input())
a=list(map(int,input().split()))
last=-1
dp=[0]*n
for i in range(n):
    k=0
    kv=-1
    for j in range(i,last,-1):
        b=a[j:i+1]
        sc=max(b)-min(b)
        if j!=0:
            sc+=dp[j-1]
        if kv<sc:
            k=j
            kv=sc
    dp[i]=kv
    last=k-1
print(dp[-1])
