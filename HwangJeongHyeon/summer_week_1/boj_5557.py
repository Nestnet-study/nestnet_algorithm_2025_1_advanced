# 아이디어 : [i번째 수까지의 결과가 j인 모든 경우의 수]로 묶어서 한번에 계산하기

# 입력
n=int(input())
a=list(map(int,input().split()))

# DP 초기화
dp=[]
for i in range(n-1):
    dp.append([0]*21)
dp[0][a[0]]=1

# 루프 바텀 업
for i in range(n-2):
    for j in range(21):
        if dp[i][j]==0:continue # 0이면 굳이 계산할 필요 없음.
        # 더하기
        if j+a[i+1]<=20:
            dp[i+1][j+a[i+1]]+=dp[i][j]
        # 빼기
        if j-a[i+1]>=0:
            dp[i+1][j-a[i+1]]+=dp[i][j]

# 결과값 출력하기
print(dp[n-2][a[-1]])
