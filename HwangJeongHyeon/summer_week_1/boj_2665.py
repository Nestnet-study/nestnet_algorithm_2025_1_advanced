"""
미로만들기
1. 그래프 탐색을 한다.
1.1 인접한 흰색방은 탐색을 하고 회색으로 바꾼다.
1.2 인접한 검은색 방은 탐색하지 않고 큐에 저장한다.
1.3 인접한 회색방은 탐색하지 않고, 저장하지 않는다.
2. 큐에 저장된 검은방에서 그래프 탐색을 한다.(1과 같은 방법)

흰색방 : 1
검은방 : 0
회색방 :-1
"""
from collections import deque

# 상수 정의
DIR4=((0,1),(1,0),(0,-1),(-1,0))

# 함수 정의
def DFS(start):
    # 리턴 값 : 도착지점(n-1,n-1)을 방문하게 되면 True, 아니면 False
    global rooms,dq
    #print(start)
    r,c=start
    rooms[r][c]=-1
    if r==n-1 and c==n-1:return True
    
    for i in range(4):
        r1,c1=r+DIR4[i][0],c+DIR4[i][1]
        if r1<0 or c1<0 or r1>=n or c1>=n:continue
        #print(r1,c1)
        if rooms[r1][c1]==1:
            rooms[r1][c1]=-1
            t=DFS((r1,c1))
            if t:return t
            continue
        if rooms[r1][c1]==0:
            rooms[r1][c1]=-1
            dq.append([r1,c1])
    return False
    

# 입력 및 초기화
n=int(input())
rooms=[]
for i in range(n):
    rooms.append(list(map(int,input())))
dq=deque()
dq.append([0,0])
dq.append('Switch')
switch=0

# 루프
while True:
    start = dq.popleft()
    if start=='Switch':
        switch+=1
        dq.append('Switch')
        continue
    t=DFS(start)
    if t:break

# 결과 출력
print(switch)
