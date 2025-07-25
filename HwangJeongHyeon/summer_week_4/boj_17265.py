# 그냥 다이나믹 문제
INF=5000 # 5^5가 연산 가능한 최대 수
n=int(input())
a=[]
high,low=[],[]
for i in range(n):
    a.append(input().split())
    high.append([-INF]*n)
    low.append([INF]*n)
high[0][0]=int(a[0][0])
low[0][0]=int(a[0][0])
for i in range(n):
    for j in range(n):
        if (i+j)%2==0: # 숫자
            if i+2<n:
                high[i+2][j]=max(high[i+2][j],eval(str(high[i][j])+a[i+1][j]+a[i+2][j]))
                low[i+2][j]=min(low[i+2][j],eval(str(low[i][j])+a[i+1][j]+a[i+2][j]))
            if i+1<n and j+1<n:
                high[i+1][j+1]=max(high[i+1][j+1],eval(str(high[i][j])+a[i+1][j]+a[i+1][j+1]),eval(str(high[i][j])+a[i][j+1]+a[i+1][j+1]))
                low[i+1][j+1]=min(low[i+1][j+1],eval(str(low[i][j])+a[i+1][j]+a[i+1][j+1]),eval(str(low[i][j])+a[i][j+1]+a[i+1][j+1]))
            if j+2<n:
                high[i][j+2]=max(high[i][j+2],eval(str(high[i][j])+a[i][j+1]+a[i][j+2]))
                low[i][j+2]=min(low[i][j+2],eval(str(low[i][j])+a[i][j+1]+a[i][j+2]))
print(high[n-1][n-1],low[n-1][n-1])
