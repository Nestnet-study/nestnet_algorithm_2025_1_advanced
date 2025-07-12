# 다이나믹 프로그래밍 : dp[i][j][k] 문자판의 i,j에 있는 k번째 단어까지 완성한 경우의 수
# 탑다운 방식으로 구현
# dp[i][j][k] = 범위 안 dp[i][j][k-1]의 합 k가 0일때 첫단어와 같으면 1 아니면 0
DIR=[(1,0),(0,1),(-1,0),(0,-1)]
def DP(x,y,z):
    global dp
    # 중복 계산 방지
    if dp[x][y][z]!=-1:return dp[x][y][z] # 이전에 방문했다면 또 값을 구할 필요 X
    dp[x][y][z]=0 # 방문했다는 것을 알리는 용도로 -1 -> 0 으로 초깃값을 바꿈

    # 예외 처리 : 문자열 s의 문자가 아닌데도 탐색한 경우
    if a[x][y]!=s[z]: # 문자열의 z번째와 같은지 확인 -> 같은 경우에만 뒤의 명령실행
        return 0

    # 루프 탈출 : k-1부터, 0번째 문자까지 탐색
    if z==0: # DP+DFS로 가장 첫번째 문자까지 도달 -> 경우를 카운트 하기 위해 1을 반환
        dp[x][y][z]=1
        return dp[x][y][z]

    # 값을 구하는 과정
    for d in DIR: # 방향(상하좌우)
        for t in range(1,k+1): #거리(1~k)
            i,j = x + (d[0]*t),y + (d[1]*t)
            if i>=0 and i<n and j>=0 and j<m and a[i][j]==s[z-1]: # 글자판 안에 있고, 글자가 같은 경우
                dp[x][y][z]+=DP(i,j,z-1)

    # 구한 값 반환
    return dp[x][y][z]

# 입력 & 초기화
# N,M,K 입력 : n,m,k (int)
n,m,k=map(int,input().split())
# 글자판 입력 : a[n][m]
a=[]
for i in range(n):
    a.append(list(input()))
# 글자 입력 : s (str)
s=input()
# dp 테이블 초기화 : dp[n][m][len(s)] = -1
dp=[]
for i in range(n):
    temp=[]
    for j in range(m):
        temp.append([-1]*len(s))
    dp.append(temp)

# 결과값 초기화
res = 0

# 모든 글자판 위의 타일에 대하여 DP(x,y,z)실행
for i in range(n):
    for j in range(m):
        res+=DP(i,j,len(s)-1)
        
# 결과값 출력
print(res)
