import sys
sys.setrecursionlimit(12000)
def dfs(r,c):
    ax=[(1,0),(0,1),(-1,0),(0,-1)]
    for u,v in ax:
        y,x=r+u,c+v
        if 0<=y and y<n and 0<=x and x<m:
            
            if chz[y][x]>0:
                chz[y][x]-=1
            elif chz[y][x]==0:
                chz[y][x]=-1
                dfs(y,x)
            
n,m=map(int,input().split())
chz=[[0]*(m+2)]

for i in range(n):
    chz.append([0]+list(map(int,input().split()))+[0])
chz.append([0]*(m+2))
n+=2
m+=2
'''
for i in range(n):
    for j in range(m):
        print(chz[i][j],end=' ')
    print()
print()
'''
#while 루프 0 안공기 -1밖공기 1~5 치즈(밖공기와 만나면 1내려)
# 모든 1~4를 5로 바꿈.
ct=0
while True:
    exist=False
    for i in range(n):
        for j in range(m):
            if chz[i][j]>0:
                chz[i][j]=5
                exist=True
    if not exist:break
    dfs(0,0)
    '''
    for i in range(n):
        for j in range(m):
            print(chz[i][j],end=' ')
        print()
    print()
    '''
    for i in range(n):
        for j in range(m):
            if chz[i][j]==-1:chz[i][j]=0
            elif chz[i][j]>0 and chz[i][j]<4:chz[i][j]=0
    ct+=1

print(ct)

