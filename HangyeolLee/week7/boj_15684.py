n,m,h = map(int,input().split())

lad = [[0] * n for _ in range(h)]

for _ in range(m):
    a,b = map(int, input().split())
    lad[a-1][b-1] = 1

answer = 4

def simulation():
    check = 1
    for i in range(n):
        x=0
        y=i
        while(x < h):
            if lad[x][y] == 1:
                y+=1
            elif y - 1 >= 0 and lad[x][y-1] == 1:
                y-=1
            x+=1
        if y == i:
            continue
        else:
            check = 0
            break

    return check

def dfs(s, x):
    global answer
    
    if x >= answer:
        return
    
    result = simulation()
    if result == 1:
        answer = x
        return
    
    for i in range(s, h):
        for j in range(n-1):
            if (lad[i][j] == 0 and (j == 0 or lad[i][j-1] == 0) and (j == n-2 or lad[i][j+1] == 0)):
                lad[i][j] = 1
                dfs(i, x+1)
                lad[i][j] = 0

dfs(0, 0)
if answer == 4:
    answer = -1

print(answer)