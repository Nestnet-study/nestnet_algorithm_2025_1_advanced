n = int(input())

arr = [[0] for _ in range(n)]

for i in range(n):
    arr[i] = input().split()

min_answer = float('inf')
max_answer = float('-inf')

def dfs(x,y,v,o):
    global min_answer, max_answer
    if x == n- 1 and y == n-1:
        if o == '-':
            v = v - int(arr[x][y])
        elif o == '*':
            v = v * int(arr[x][y])
        elif o == '+':
            v = v + int(arr[x][y])
        
        if v < min_answer:
            min_answer = v
        if v > max_answer:
            max_answer = v
        return
    
    if arr[x][y] == '+':
        o = '+'
    elif arr[x][y] == '*':
        o = '*'
    elif arr[x][y] == '-':
        o = '-'
    else:
        if o == '-':
            v = v - int(arr[x][y])
        elif o == '*':
            v = v * int(arr[x][y])
        elif o == '+':
            v = v + int(arr[x][y])
        else:
            v = v

    if x + 1 < n:
        dfs(x+1,y,v,o)
    if y + 1 < n:
        dfs(x, y+1,v,o)

dfs(0,0,int(arr[0][0]),'')

print(max_answer, min_answer)

