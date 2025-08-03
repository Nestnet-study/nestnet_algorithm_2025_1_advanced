from collections import deque

n = int(input())
k = int(input())

field = [[0] * n for _ in range(n)]
field[0][0] = 1 # 지렁이 1

apple = [0] * k
for i in range(k):
    x,y = map(int, input().split())
    field[x-1][y-1] = 5 # 사과 5

l = int(input())

way = 1 # 방향을 나타냄 1: 오른쪽, 2: 아래, 3: 왼쪽, 4: 위쪽
cur_t = 0 # 현재 시간

head = [0,0]
tail = [0,0]

lava = deque()

def die():
    print(cur_t)
    exit()

def head_move(w):
    global cur_t

    cur_t+=1

    lava.appendleft(w)
    if w == 1:
        head[1]+=1
        if head[1] >= n or field[head[0]][head[1]] == 1:
            die()
    elif w == 2:
        head[0]+=1
        if head[0] >= n or field[head[0]][head[1]] == 1:
            die()
    elif w == 3:
        head[1]-=1
        if head[1] < 0 or field[head[0]][head[1]] == 1:
            die()
    else:
        head[0]-=1
        if head[0] < 0 or field[head[0]][head[1]] == 1:
            die()
    if field[head[0]][head[1]] != 5:
        tail_move(lava.pop())
    field[head[0]][head[1]] = 1

def tail_move(w):
    field[tail[0]][tail[1]] = 0

    if w == 1:
        tail[1]+=1
    elif w == 2:
        tail[0]+=1
    elif w == 3:
        tail[1]-=1
    else:
        tail[0]-=1
    
spin = [[0,0] for _ in range(l) ]

for i in range(l):
    t, c = input().split()

    spin[i][0] = t
    spin[i][1] = c

for i in range(l):
    t = spin[i][0]
    c = spin[i][1]

    t = int(t)-cur_t

    while(t > 0):
        head_move(way)
        t-=1

    if c == 'D':
        way+=1
    else:
        way-=1
    if way > 4:
        way = 1
    elif way < 1:
        way = 4

while(1):    
    head_move(way)

