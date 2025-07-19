import sys
input = sys.stdin.readline
from collections import deque

S = int(input())


queue = deque()
queue.append([1,1,1]) # [화면, 클립보드, 몇초 후]

check = [[0,0,0] for _ in range(10000)]

while(queue):
    x,y,z = queue.popleft()
    if check[x][0] == 1 and check[x][1] == y and check[x][2] == z:
        continue
    else:
        check[x][0] = 1
        check[x][1] = y
        check[x][2] = z
    if x == S:
        print(z)
        break
    if x != y:
        queue.append([x,x,z+1])
    queue.append([x+y,y,z+1])
    if x > 0:
        queue.append([x-1,y,z+1])

