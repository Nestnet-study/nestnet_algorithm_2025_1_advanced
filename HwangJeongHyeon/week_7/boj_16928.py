"""
알고리즘 :
1. 사다리 각 1개씩 가능 즉 리스트로 저장
2. 방문한 곳은 다시 가지 않음.
"""
from collections import deque
n,m=map(int,input().split())

ladder = list(range(100))
for i in range(n):
    a,b=map(int,input().split())
    a-=1
    b-=1
    ladder[a]=b
for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    ladder[a]=b

dq=deque()
dq.append([0,0])
visited = [1]+[0]*99

flag = False
x,y,z=0,0,0
#print(len(dq))
while len(dq)>0:
    #input()
    x,y=dq.popleft()
    #print(x,y)
    #print(dq)
    for i in range(1,7):
        if x+i<100:
            z = ladder[x+i]
            if visited[z]:continue
            if z==99:
                flag = True
                break;
            visited[z]=True
            dq.append([z,y+1])
    if flag:break;
print(y+1)
