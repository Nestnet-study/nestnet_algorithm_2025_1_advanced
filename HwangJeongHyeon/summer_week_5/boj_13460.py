from collections import deque
DIR=[(0,1),(1,0),(-1,0),(0,-1)]
n,m = map(int,input().split())
a=[]
for i in range(n):
    a.append(list(input()))
st = set()
dq = deque()

# r,b위치 저장
r,b=(0,0),(0,0)
for i in range(n):
    for j in range(m):
        if a[i][j]=='R':
            r=[i,j]
            a[i][j]='.'
        elif a[i][j]=='B':
            b=[i,j]
            a[i][j]='.'
st.add(n*m*m*r[0]+n*m*r[1]+m*b[0]+b[1])
dq.append([r,b,0])
res = -1
while len(dq):
    r,b,c=dq.popleft()
    #print(r,b,c)
    # 한쪽 방향으로 기울이는 동작
    for d in range(4):
        
        r1,b1=list(r),list(b) ; #print(d,r1,b1)
        nr=[DIR[d][0]+r1[0],DIR[d][1]+r1[1]]
        nb=[DIR[d][0]+b1[0],DIR[d][1]+b1[1]]
        # 이 과정이 끝나면 R은 O에 있거나 벽에 막히고, B는 벽이나 O에 막힘.
        while (a[nr[0]][nr[1]] in ['O','.'] and nr!=b1 and a[r1[0]][r1[1]]!='O') or (a[nb[0]][nb[1]] == '.' and nb!=r1):
            # R이 움직임.
            if (a[nr[0]][nr[1]]=='.' or a[nr[0]][nr[1]]=='O') and nr!=b1 and a[r1[0]][r1[1]]!='O':
                r1=list(nr)
                nr=[r1[0]+DIR[d][0],r1[1]+DIR[d][1]]
            # B가 움직임.
            if a[nb[0]][nb[1]]=='.' and nb!=r1:
                b1=list(nb)
                nb=[b1[0]+DIR[d][0],b1[1]+DIR[d][1]]
        #print(r1,b1)
        # B의 다음 위치가 O이면 실패
        if a[nb[0]][nb[1]]=='O':
            continue
        # R의 현재 위치가 O이면 성공
        if a[r1[0]][r1[1]]=='O':
            res=c+1
            break
        # 둘다 벽에 막히면 dq에 넣음. 단 처음일 때만
        if not n*m*m*r1[0]+n*m*r1[1]+m*b1[0]+b1[1] in st:
            st.add(n*m*m*r1[0]+n*m*r1[1]+m*b1[0]+b1[1])
            dq.append([r1,b1,c+1])
    if res!=-1:
        break
if res>10:
    print(-1)
else:
    print(res)
