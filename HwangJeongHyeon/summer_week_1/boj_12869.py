# 아이디어 : [1 3 2]->[1 2 3] == [1 2 3]->[1 3 2]는 동일하기에 같은 계산을 두번 할 필요 없음.
# 하나가 남았을 때 1만 계속하는 경우까진 찾을 필요 없음 BFS
# Deque를 통해서 (X,Y,Z,W) X,Y,Z는 뮤탈리스크의 체력, W는 사용한 타입이다.
# 타입이 w일 때 w보다 작은 것은 더이상 사용할 수 없다.
"""
1 2 3 : 0
1 3 2 : 1
2 1 3 : 2
2 3 1 : 3
3 1 2 : 4 
3 2 1 : 5
"""
from collections import deque

# 입력
n=int(input())
a=list(map(int,input().split()))

# 초기화
a=a+[0]*(3-len(a))
dq=deque()
dq.append(a+[0])
dq.append('NextAttack!!')

# 루프
attack=0
while True:
    x=dq.popleft()
    if x=='NextAttack!!':
        attack+=1
        dq.append('NextAttack!!')
        continue
    x,y,z,w=x
    if x<=0 and y<=0 and z<=0:
        break;
    dq.append([x-1,y-3,z-9,5])
    if w==5:continue
    dq.append([x-1,y-9,z-3,4])
    if w==4:continue
    dq.append([x-3,y-1,z-9,3])
    if w==3:continue
    dq.append([x-3,y-9,z-1,2])
    if w==2:continue
    dq.append([x-9,y-1,z-3,1])
    if w==1:continue
    dq.append([x-9,y-3,z-1,0])

# 결과
print(attack)
