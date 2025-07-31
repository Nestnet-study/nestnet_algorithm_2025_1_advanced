from collections import deque
DIR=[[0,1],[1,0],[0,-1],[-1,0]]
n=int(input())
k=int(input())
apl=[]
for i in range(k):
    apl.append(list(map(lambda x: int(x)-1,input().split())))
l=int(input())
rot=deque()
for i in range(l):
    t,r=input().split()
    t=int(t)
    rot.append((t,r))
d=0
size=1
dq=deque()
dq.append([0,0])
time=0
while True:
    time+=1
    nxt=[dq[-1][0]+DIR[d][0],dq[-1][1]+DIR[d][1]]
    if nxt in dq or nxt[0]<0 or nxt[1]<0 or nxt[0]>=n or nxt[1]>=n:
        break
    dq.append(nxt)
    if nxt in apl:
        del apl[apl.index(nxt)]
    else:
        dq.popleft()
    
    if len(rot) and rot[0][0]==time:
        t,r=rot.popleft()
        if r=='D':
            d=(d+1)%4
        else:
            d=(d+3)%4
    
print(time)
"""
13
[ ][ ][ ][ ][ ][ ][ ][<][ ][ ]
[ ][ ][@][@][ ][@][@][A][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]






"""
