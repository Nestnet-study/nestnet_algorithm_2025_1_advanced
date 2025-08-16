import sys
input=sys.stdin.readline

n,m,h=map(int,input().rstrip().split())

arr=[[0]*(n+2) for _ in range(h+1)]
for _ in range(m):
    li,lj=map(int,input().rstrip().split())
    arr[li][lj]=1

# 사다리 놓을 후보 저장
pos=[]
for i in range(1,h+1):
    for j in range(1,n+1):
        if arr[i][j]==0 and arr[i][j-1]==0 and arr[i][j+1]==0:
            pos.append((i,j))
CNT=len(pos)

# 사다리 태워서 시작점과 끝점이 같은지 확인
def check():
    for sj in range(1,n+1):
        j=sj
        for i in range(1,h+1):
            # 우측 이동
            if arr[i][j]==1:
                j+=1
            # 좌측 이동
            elif arr[i][j-1]==1:
                j-=1
        if j!=sj:
            return False
    return True

# DFS: 사다리 놓고, 검사하고(check), 빼고를 반복
def dfs(n,s):
    global ans
    # 가지치기
    if ans==1:
        return
    if n==cnt:
        if check():
            ans=1
        return

    for j in range(s,CNT):
        li,lj=pos[j]
        if arr[li][lj-1]==0 and arr[li][lj+1]==0:
            arr[li][lj]=1 # 사다리 놓기
            dfs(n+1,j+1) # 검사하기
            arr[li][lj]=0 # 사다리 빼기

# 추가하는 사다리 개수 0~3 시행 => 안되면 -1이 정답
for cnt in range(4):
    ans=0
    dfs(0,0)
    if ans==1:
        ans=cnt
        break
else:
    ans=-1
print(ans)