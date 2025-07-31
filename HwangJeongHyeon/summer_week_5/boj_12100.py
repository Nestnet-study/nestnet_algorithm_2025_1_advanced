import copy
def Move(bd,t=5):
    '''
    print(t)
    for i in range(n):
        print(bd[i])
    '''
    if t==0:
        res = 0
        for i in range(n):res=max(res,max(bd[i]))
        return res
    res=0
    
    
    
    # 윗 방향 (-1,0)
    nb=copy.deepcopy(bd)
    st=set()
    for i in range(1,n):
        for j in range(n):
            for k in range(i-1,-1,-1):
                if nb[k][j]==0:# 빈공간 : 이동
                    nb[k][j],nb[k+1][j]=nb[k+1][j],0
                elif nb[k][j]==nb[k+1][j] and not k*n+j in st:
                    # 같고, 합쳐지지 않은 수가 있다 : 결합 후 정지
                    st.add(k*n+j)
                    nb[k][j]*=2
                    nb[k+1][j]=0
                    break
                else: # 다음 위치에 상관 없는 다른 숫자가 있다 : 정지
                    break
    res=max(res,Move(nb,t-1))
    # 아랫 방향 (1,0)
    nb=copy.deepcopy(bd)
    st=set()
    for i in range(n-2,-1,-1):
        for j in range(n):
            for k in range(i+1,n):
                if nb[k][j]==0:# 빈공간 : 이동
                    nb[k][j],nb[k-1][j]=nb[k-1][j],0
                elif nb[k][j]==nb[k-1][j] and not k*n+j in st:
                    # 같고, 합쳐지지 않은 수가 있다 : 결합 후 정지
                    st.add(k*n+j)
                    nb[k][j]*=2
                    nb[k-1][j]=0
                    break
                else: # 다음 위치에 상관 없는 다른 숫자가 있다 : 정지
                    break
    res=max(res,Move(nb,t-1))
    # 오른쪽 방향(0,1)
    nb=copy.deepcopy(bd)
    st=set()
    for i in range(n-2,-1,-1):
        for j in range(n):
            for k in range(i+1,n):
                if nb[j][k]==0:# 빈공간 : 이동
                    nb[j][k],nb[j][k-1]=nb[j][k-1],0
                elif nb[j][k]==nb[j][k-1] and not j*n+k in st:
                    # 같고, 합쳐지지 않은 수가 있다 : 결합 후 정지
                    st.add(j*n+k)
                    nb[j][k]*=2
                    nb[j][k-1]=0
                    break
                else: # 다음 위치에 상관 없는 다른 숫자가 있다 : 정지
                    break
    res=max(res,Move(nb,t-1))
    # 왼쪽 방향 (0,-1)
    nb=copy.deepcopy(bd)
    st=set()
    for i in range(1,n):
        for j in range(n):
            for k in range(i-1,-1,-1):
                if nb[j][k]==0:# 빈공간 : 이동
                    nb[j][k],nb[j][k+1]=nb[j][k+1],0
                elif nb[j][k]==nb[j][k+1] and not j*n+k in st:
                    # 같고, 합쳐지지 않은 수가 있다 : 결합 후 정지
                    st.add(j*n+k)
                    nb[j][k]*=2
                    nb[j][k+1]=0
                    break
                else: # 다음 위치에 상관 없는 다른 숫자가 있다 : 정지
                    break
    res=max(res,Move(nb,t-1))
    return res
n=int(input())

a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
print(Move(a))
