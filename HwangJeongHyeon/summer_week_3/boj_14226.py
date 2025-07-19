"""
문제
이모티콘 S개를 만드는 최소 시간
현재 이모티콘의 개수를 n개라고 하면
1. n을 m에 저장
2. m을 붙여넣기
3. n--
S의 최대가 1000으로 작다.
n,m을 2000,2000정도로 크게 잡아준다고 해도 4*10^6 밖에 안되기에 가능
BFS + DP
"""
from collections import deque
s=int(input())
n=1
m=0
dq=deque()
dq.append((n,m,0))
dp=[]
for i in range(2025):
    dp.append([-1]*2025)
dp[n][m]=0
while len(dq):
    n,m,t=dq.popleft()
    # n이 S와 같은지 확인
    if n==s:break
    
    # n을 m에 저장 | 단 n이 목표값보다 작을 때만 복붙가능
    if n<s:
        if dp[n][n]==-1:
            dp[n][n]=t+1
            dq.append((n,n,t+1))
        if dp[n+m][m]==-1:
            dp[n+m][m]=t+1
            dq.append((n+m,m,t+1))
    if n>1:
        if dp[n-1][m]==-1:
            dp[n-1][m]=t+1
            dq.append((n-1,m,t+1))
    
print(t)
