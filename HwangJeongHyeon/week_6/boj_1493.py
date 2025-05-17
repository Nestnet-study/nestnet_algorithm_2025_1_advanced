import math
def Box(bx):
    global count
    #print(bx,count)
    if 0 in bx:return 0;
    # bx[0],bx[1],bx[2]
    mi=0
    for i in range(1,3):
        if bx[mi]<bx[i]:
            mi=i
    for t in range(20):
        if (1<<t)>bx[mi]:
            t-=1
            break
    if bx[0]==bx[1] and bx[1]==bx[2] and bx[0]==(1<<t) and cubes[t]:
        cubes[t]-=1
        if count!=-1:
            count+=1
        return 0
    bx1,bx2=list(bx),list(bx)
    if bx[mi]==(1<<t):t-=1
    if t==-1:
        count = -1
        return -1;
    bx1[mi],bx2[mi] = 1<<t,bx[mi]-(1<<t)
    if -1==Box(bx1):return -1
    if -1==Box(bx2):return -1

l,w,h = map(int,input().split())
n = int(input())
cubes = [0]*20
count = 0
for i in range(n):
    a,b=map(int,input().split())
    cubes[a]=b

Box((l,w,h))
print(count)
