# s는 방문한 곳을 비트마스킹한 것,j는 현재 위치
def topDown(s,j):
    if dp[s][j]==-1: # 처음 topDown(s,j)를 실행했다면 (메모리제이션) ABCD ACBD
        if s==(1<<n) - 1: # S가 11...111 이라면 즉 모든 정점을 순환하였다면
            if w[j][0]==0:return INF # 현재 위치에서 0인 위치로 갈 수 없으면 제외
            dp[s][j]=w[j][0] # 현재 위치에서 0인 위치로 가는 거리
            return dp[s][j]
        m=INF
        for i in range(n):
            if ((s & (1<<i)) == 0 and w[j][i]!=0): # 아직 방문 안했고, 갈 수 있다면
                m=min(m,topDown(s | (1<<i),i) + w[j][i]) # 다음 정점을 방문한 경우의 최소
        dp[s][j]=m
    return dp[s][j]
# 무한 정의
INF = 2**31-1
# 입력
n=int(input())
w=[]
for i in range(n):
    w.append(list(map(int,input().split())))

#dp테이블 셋팅
dp=[]
for i in range(2**n):
    dp.append([-1]*n)
print(topDown(1,0))
