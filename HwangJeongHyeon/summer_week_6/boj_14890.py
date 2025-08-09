# 이전보다 높이가 -1이면 설치가 된 상태에서 slope = -L 단 L>=0일때 

def test(b):
    before=b[0]
    slope=0
    failflag=False
    #print(b)
    for j in range(n):
        #print(b[j],slope)
        if b[j]-before == 0:
            None
        elif b[j]-before == -1 and slope >= 0: # \\를 설치할 조건
            slope=-l
        elif b[j]-before == 1 and slope >= l: # //를 설치할 조건
            slope=0
        else: # 실패
            failflag=True
            break
        slope+=1
        before=b[j]
    if slope<0:failflag=True
    
    if failflag:
        return 0
    return 1

n,l=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
res=0
for i in range(n):
    b=list(a[i])
    res+=test(b)
    b=[]
    for j in range(n):
        b.append(a[j][i])
    res+=test(b)
print(res)
"""

L=2
1 1 2 1 1 1 1 2 3
0 1 2 1-1 0 1 2 1
/ / 2 \ \ / / 2
"""
