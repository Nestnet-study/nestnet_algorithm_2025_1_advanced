import sys
input=sys.stdin.readline
from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(ch):
    global ans

    q=deque([[0,0]])
    ch[0][0]=1

    while q:
        x,y=q.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # EARLY RETURN: 범위 밖이거나, 벽이거나, 이미 방문한 경우
            if nx<0 or nx>=h+2 or ny<0 or ny>=w+2 or graph[nx][ny]=='*' or ch[nx][ny]:
                continue
            # CASE 1: 문
            if 'A'<=graph[nx][ny]<='Z':
                if graph[nx][ny].lower() not in key:
                    continue
            # CASE 2: 키
            elif 'a'<=graph[nx][ny]<='z':
                if graph[nx][ny] not in key:
                    key[graph[nx][ny]]=1
                    # 방문여부 초기화
                    ch=[[0]*(w+2) for _ in range(h+2)]
            # CASE 3: 문서
            elif graph[nx][ny]=='$' and (nx,ny) not in ch_doc:
                ans+=1
                ch_doc.append((nx,ny))

            ch[nx][ny]=1
            q.append([nx,ny])


t=int(input().rstrip())
for _ in range(t):
    h,w=map(int,input().rstrip().split())
    graph=['.'+input().rstrip()+'.' for _ in range(h)]
    graph=['.'*(w+2)]+graph+['.'*(w+2)]
    ch=[[0]*(w+2) for _ in range(h+2)]
    key={}
    ch_doc=[]

    for k in input().rstrip():
        if k!=0:
            key[k]=1
    ans=0
    bfs(ch)
    print(ans)