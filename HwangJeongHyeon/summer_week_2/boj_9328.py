# 문제
"""
1. 최대 얻을 수 있는 문서의 개수를 출력하시오.
2. 플레이어는 빌딩 밖에서 시작한다.
3. 밖은 모두 뚫려있다.
4. 열쇠는 소문자로 표시되며 각각 대응되는 문을 열 수 있다.
5. 시작하기 전에 가지고 있는 열쇠가 주어진다. 없으면 0이 주어진다.
6. 2<=w,h<=100
"""
# 알고리즘
"""
준비 작업
1. 가지고 있는 모든 열쇠 사용해서 '.'으로 만들기
2. 모든 문을 열쇠에 따라 저장
3. 밖에서 들어올수 있는 구간 덱에 넣기
탐색
1. 덱에서 위치 얻어오기
2. 현재 위치에 문서가 있으면 결과값을 올리기
3. 현재 위치에 열쇠가 있으면 열쇠에 대응되는 모든 문에서 외곽이거나 방문한 곳이 옆에 있으면 덱에 넣기
4. 근처 4방향 중 방문할 수 있는 곳 덱에 넣기
5. 덱에 넣은 위치를 visited에 표시
결과 출력
"""
# 코드
from collections import deque
DIR=[(1,0),(0,1),(-1,0),(0,-1)]
T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    a=[]
    for i in range(n):
        a.append(list(input()))
    dq=deque()
    visited=[]
    for i in range(n):
        visited.append([False]*m)
    res=0
    #=============미리 얻은 열쇠 처리=================
    s=input()
    if s!='0':
        s=list(map(lambda x: ord(x)-ord('a'),s))
        for i in range(n):
            for j in range(m):
                if ord(a[i][j])-ord('A') in s:
                    a[i][j]='.'
    #=============대응되는 문의 위치 저장==============
    doors=[]
    for i in range(30):doors.append([])
    for i in range(n):
        for j in range(m):
            if a[i][j].isupper():
                doors[ord(a[i][j])-ord('A')].append((i,j))
    #========밖에서 들어올 수 있는 위치 덱에 넣기========
    for i in range(n):
        for j in range(m):
            if (i==0 or j==0 or i==n-1 or j==m-1) and\
               (a[i][j]=='.' or a[i][j]=='$' or a[i][j].islower()):
                dq.append((i,j))
                visited[i][j]=True
    #======================탐색=====================
    while len(dq):
        i,j=dq.popleft()
        if a[i][j]=='$':res+=1
        if a[i][j].islower():
            key=ord(a[i][j])-ord('a')
            for x,y in doors[key]:
                if visited[x][y]:continue
                a[x][y]='.'
                if x==0 or y==0 or x==n-1 or y==m-1:
                    dq.append((x,y))
                    visited[x][y]=True
                    continue
                for dx,dy in DIR:
                    u,v=x+dx,y+dy
                    if visited[u][v]:
                        dq.append((x,y))
                        visited[x][y]=True
                        break
        for dx,dy in DIR:
            u,v=i+dx,j+dy
            if u<0 or v<0 or u>=n or v>=m or\
               visited[u][v] or a[u][v].isupper() or a[u][v]=='*':continue
            dq.append((u,v))
            visited[u][v]=True
    print(res)
