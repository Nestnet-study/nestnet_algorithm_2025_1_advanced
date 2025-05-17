power=[[0,2,2,2,2],
       [0,1,3,4,3],
       [0,3,1,3,4],
       [0,4,3,1,3],
       [0,3,4,3,1]]
a=list(map(int,input().split()))
a.pop(-1)
n=len(a)
mem=[]
for i in range(n+1):
    tmp=[]
    for j in range(5):
        tmp.append([-1]*5)
    mem.append(tmp)
mem[0][0][0]=0
for i in range(n):
    for j in range(5):
        for k in range(5):
            if mem[i][j][k]!=-1:
                if k!=a[i]:#왼쪽 바꿈
                    new=mem[i][j][k]+power[j][a[i]]
                    if mem[i+1][a[i]][k]==-1 or mem[i+1][a[i]][k]>new:
                        mem[i+1][a[i]][k]=new
                if j!=a[i]:
                    new=mem[i][j][k]+power[k][a[i]]
                    if mem[i+1][j][a[i]]==-1 or mem[i+1][j][a[i]]>new:
                        mem[i+1][j][a[i]]=new
m = -1
for i in range(5):
    for j in range(5):
        #print(mem[n][i][j])
        if m==-1 or (mem[n][i][j]<m and mem[n][i][j]!=-1):
            m=mem[n][i][j]
print(m)
