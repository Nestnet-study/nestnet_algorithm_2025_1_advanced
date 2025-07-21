# import copy
import sys
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
graph=list(list(map(int,input().rstrip().split())) for _ in range(n))

d=[[0]*m for _ in range(n)]
# d[0]=copy.deepcopy(graph[0])
d[0]=graph[0][:]


for i in range(1,m):
    d[0][i]+=d[0][i-1]

for i in range(1,n):
    tmp_l_to_r=[0]*m # 좌->우
    tmp_r_to_l=[0]*m # 우->좌
    
    # 첫 원소와 마지막 원소의 경우, 위에서 오는 경우 밖에 없음
    tmp_l_to_r[0]=graph[i][0]+d[i-1][0]
    tmp_r_to_l[-1]=graph[i][-1]+d[i-1][-1]
    for j in range(1,m):
        tmp_l_to_r[j]=graph[i][j]+max(d[i-1][j],tmp_l_to_r[j-1]) # 현재 위치 + max(위 최대, 좌->우)
        tmp_r_to_l[m-1-j]=graph[i][m-1-j]+max(d[i-1][m-1-j],tmp_r_to_l[m-j]) # 현재 위치 + max(위 최대, 우->좌)

    tmp=[max(tmp_l_to_r[k],tmp_r_to_l[k]) for k in range(m)]
    # d[i]=copy.deepcopy(tmp)
    d[i]=tmp[:]


print(d[n-1][m-1])