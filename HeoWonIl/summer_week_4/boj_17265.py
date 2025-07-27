import sys
input=sys.stdin.readline

n=int(input().rstrip())
graph=[list(input().rstrip().split()) for _ in range(n)]

dp1=[[0]*n for _ in range(n)]
dp2=[[0]*n for _ in range(n)]
dp1[0][0]=int(graph[0][0])
dp2[0][0]=int(graph[0][0])


def calc(op1,op,op2):
    if op=='+':
        return op1+op2
    elif op=='-':
        return op1-op2
    elif op=='*':
        return op1*op2


for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            continue
        if not graph[i][j].isdigit():
            continue
        val=int(graph[i][j])
        max_val=int(-1e9)
        min_val=int(1e9)
        if 0<=i-2<n and 0<=j<n:
            max_val=max(max_val,calc(int(dp1[i-2][j]),graph[i-1][j],val))
            min_val=min(min_val,calc(int(dp2[i-2][j]),graph[i-1][j],val))
        if 0<=i<n and 0<=j-2<n:
            max_val=max(max_val,calc(int(dp1[i][j-2]),graph[i][j-1],val))
            min_val=min(min_val,calc(int(dp2[i][j-2]),graph[i][j-1],val))
        if 0<=i-1<n and 0<=j-1<n:
            max_val=max(max_val,calc(int(dp1[i-1][j-1]),graph[i][j-1],val))
            min_val=min(min_val,calc(int(dp2[i-1][j-1]),graph[i][j-1],val))
            max_val=max(max_val,calc(int(dp1[i-1][j-1]),graph[i-1][j],val))
            min_val=min(min_val,calc(int(dp2[i-1][j-1]),graph[i-1][j],val))
        dp1[i][j]=max_val
        dp2[i][j]=min_val

print(dp1[n-1][n-1],dp2[n-1][n-1],sep=' ')
