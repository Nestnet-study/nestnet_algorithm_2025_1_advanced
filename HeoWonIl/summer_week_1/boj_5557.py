import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().rstrip().split()))

ans=0
d={}

def dfs(idx,sum):
    global ans
    # 가지치기
    if sum<0 or sum>20:
        return 0

    # 종료조건
    if idx==n-1:
        return 1 if sum==arr[idx] else 0

    # 메모이제이션
    if (idx,sum) in d:
        return d[(idx,sum)]

    d[(idx,sum)]=dfs(idx+1,sum-arr[idx])+dfs(idx+1,sum+arr[idx])

    return d[(idx,sum)]

print(dfs(1,arr[0]))