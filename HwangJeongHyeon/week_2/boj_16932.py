from collections import deque
n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
M=0
for y in range(n):
    for x in range(m):
        if a[y][x]==0:
            ct=0
            dq=deque()
            dq.append((y,x))
            while len(dq)!=0:
                ct+=1
                i,j=dq.pop()
                if i>0 and a[i-1][j]==1:
                    a[i-1][j]=-1
                    dq.append((i-1,j))
                if j>0 and a[i][j-1]==1:
                    a[i][j-1]=-1
                    dq.append((i,j-1))
                if i<n-1 and a[i+1][j]==1:
                    a[i+1][j]=-1
                    dq.append((i+1,j))
                if j<m-1 and a[i][j+1]==1:
                    a[i][j+1]=-1
                    dq.append((i,j+1))
            dq.append((y,x))
            while len(dq)!=0:
                i,j=dq.pop()
                if i>0 and a[i-1][j]==-1:
                    a[i-1][j]=1
                    dq.append((i-1,j))
                if j>0 and a[i][j-1]==-1:
                    a[i][j-1]=1
                    dq.append((i,j-1))
                if i<n-1 and a[i+1][j]==-1:
                    a[i+1][j]=1
                    dq.append((i+1,j))
                if j<m-1 and a[i][j+1]==-1:
                    a[i][j+1]=1
                    dq.append((i,j+1))
            M=max(M,ct)
print(M)
