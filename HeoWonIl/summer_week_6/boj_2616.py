import sys
input=sys.stdin.readline

n=int(input())
arr=[0]+list(map(int,input().rstrip().split()))
m=int(input())

prefix_sum=[0]
for i in range(1,n+1):
    prefix_sum.append(prefix_sum[i-1]+arr[i])

d=[[0]*(n+1) for _ in range(4)]
for i in range(1,4):
    for j in range(i*m,n+1):
        d[i][j]=max(d[i-1][j-m]+prefix_sum[j]-prefix_sum[j-m],d[i][j-1])

print(d[3][n])