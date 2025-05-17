from collections import deque
def main(n,m):
    a=[]
    for i in range(n):
        a.append(list(input()))
    t=0
    graph=[]
    dic = dict()
    r,c=0,0
    for i in range(n):
        for j in range(m):
            if a[i][j]=='o':
                r,c=i,j
            elif a[i][j]=='*':
                dic[(i,j)]=t
                t+=1
    for k in range(1<<t):
        graph.append([])
        for i in range(n):
            graph[k].append([])
            for j in range(m):
                graph[k][i].append(a[i][j])
                if a[i][j]=='o': graph[k][i][j]='.'


    dq=deque([[0,r,c,0]]);graph[0][r][c]='x'
    d=[[1,0],[-1,0],[0,1],[0,-1]]
    breakFlag=False
    while len(dq)>0:
        bit,r,c,dist=dq.pop()
        if bit==(1<<t)-1:
            print(dist)
            breakFlag=True
            break
        #print(bin(bit),r,c,dist)
        for d1,d2 in d:
            x,y=d1+r,d2+c
            if 0<=x and x<n and 0<=y and y<m and graph[bit][x][y]!='x':
                if graph[bit][x][y]=='*':
                    ti=dic[(x,y)]
                    if not ((1<<ti) & (bit)):
                        graph[(bit | (1<<ti))][x][y]='x'
                        dq.append([bit | (1<<ti),x,y,dist+1])
                        continue
                graph[bit][x][y]='x'
                dq.appendleft([bit,x,y,dist+1])
    if not breakFlag:
        print(-1)
while True:
    m,n=map(int,input().split())
    if n==0 and m==0: break
    main(n,m)








