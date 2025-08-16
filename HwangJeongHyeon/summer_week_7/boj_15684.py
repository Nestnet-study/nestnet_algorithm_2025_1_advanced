'''
1 2 3 4 5
|-|0|0|0| 1
|0|0|-|0| 2
|0|-|0|0| 3
|0|0|0|0| 4
|-|0|0|-| 5
|0|0|0|0| 6
'''
def fn():
    b=list(range(m))
    for i in range(n):
        for j in range(m-1):
            if a[i][j]==1:
                b[j],b[j+1]=b[j+1],b[j]
    c=list(range(m))
    if b==c:
        return True
    return False
    
m,h,n=map(int,input().split())
a=[]
for i in range(n):
    a.append([0]*(m-1))
for i in range(h):
    x,y=map(int,input().split())
    a[x-1][y-1]=1
mn=4
if fn():
    mn=0
for x1 in range(n):
    for y1 in range(m-1):
        if(a[x1][y1]==1)or(y1!=0 and a[x1][y1-1]==1)or(y1!=m-2 and a[x1][y1+1]==1):continue
        a[x1][y1]=1
        if fn():
            mn=min(mn,1)
        for x2 in range(x1,n):
            for y2 in range(m-1):
                if x1==x2 and y1>=y2:continue
                if(a[x2][y2]==1)or(y2!=0 and a[x2][y2-1]==1)or(y2!=m-2 and a[x2][y2+1]==1):continue
                a[x2][y2]=1
                if fn():
                    mn=min(mn,2)
                for x3 in range(x2,n):
                    for y3 in range(m-1):
                        if x2==x3 and y2>=y3:continue
                        if(a[x3][y3]==1)or(y3!=0 and a[x3][y3-1]==1)or(y3!=m-2 and a[x3][y3+1]==1):continue
                        a[x3][y3]=1
                        if fn():
                            mn=min(mn,3)
                        a[x3][y3]=0
                a[x2][y2]=0
        a[x1][y1]=0
if mn==4:
    print(-1)
else:
    print(mn)
