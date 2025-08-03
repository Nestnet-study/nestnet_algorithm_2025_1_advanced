import sys
import copy
input = sys.stdin.readline

n = int(input())

miro = [0] * n
for i in range(n):
    miro[i] = list(map(int, input().split()))

before_miro = copy.deepcopy(miro)
answer = 0 
for i in range(n):
    for j in range(n):
        if answer < miro[i][j]:
            answer = miro[i][j]

def right():
    global before_miro, answer
    before_miro = copy.deepcopy(miro)
    for i in range(n):
        stack = []
        check = miro[i][n-1]
        if check != 0:
            stack.append(check)
        for j in range(n-2, -1, -1):
            if miro[i][j] != 0:
                if check == miro[i][j] and stack:
                    var = stack.pop()*2
                    if var > answer:
                        answer = var
                    stack.append(var)
                    check = 0
                else:
                    check = miro[i][j]
                    stack.append(miro[i][j])
        l = len(stack)
        j = 0
        while(j<n):
            if n-j > l:
                miro[i][j] = 0
            else:
                miro[i][j] = stack.pop()
            j+=1

def left():
    global before_miro, answer
    before_miro = copy.deepcopy(miro)
    for i in range(n):
        stack = []
        check = miro[i][0]
        if check != 0:
            stack.append(check)
        for j in range(1, n):
            if miro[i][j] != 0:
                if check == miro[i][j] and stack:
                    var = stack.pop()*2
                    if var > answer:
                        answer = var
                    stack.append(var)
                    check = 0
                else:
                    check = miro[i][j]
                    stack.append(miro[i][j])
        l = len(stack)
        j = 0
        while(j < n):
            if n-l > j:
                miro[i][n-j-1] = 0
            else:
                miro[i][n-j-1] = stack.pop()
            j += 1

def down():
    global before_miro, answer
    before_miro = copy.deepcopy(miro)
    for j in range(n):
        stack = []
        # 밑에서부터 시작
        check = miro[n-1][j]
        if check != 0:
            stack.append(check)
        for i in range(n-2, -1, -1):
            if miro[i][j] != 0:
                if check == miro[i][j] and stack:
                    var = stack.pop() * 2
                    if var > answer:
                        answer = var
                    stack.append(var)
                    check = 0
                else:
                    check = miro[i][j]
                    stack.append(miro[i][j])
        # 밑쪽부터 채우기 : stack의 길이만큼은 병합된 값, 나머지는 0
        l = len(stack)
        for i in range(n):
            if i < n - l:
                miro[i][j] = 0
            else:
                miro[i][j] = stack.pop()

def up():
    global before_miro, answer
    before_miro = copy.deepcopy(miro)
    for j in range(n):
        stack = []
        # 위쪽부터 시작
        check = miro[0][j]
        if check != 0:
            stack.append(check)
        for i in range(1, n):
            if miro[i][j] != 0:
                if check == miro[i][j] and stack:
                    var = stack.pop() * 2
                    if var > answer:
                        answer = var
                    stack.append(var)
                    check = 0
                else:
                    check = miro[i][j]
                    stack.append(miro[i][j])
        # 위쪽부터 채우기 : stack의 길이만큼은 병합된 값, 나머지는 0
        l = len(stack)
        for i in range(n):
            if i < l:
                miro[i][j] = stack[i]
            else:
                miro[i][j] = 0

def simulation(depth):
    global miro
    if depth == 0:
        return
    state = copy.deepcopy(miro)

    right()
    simulation(depth - 1)
    miro = copy.deepcopy(state)  # 상태 복원

    left()
    simulation(depth - 1)
    miro = copy.deepcopy(state)
    
    up()
    simulation(depth - 1)
    miro = copy.deepcopy(state)
    
    down()
    simulation(depth - 1)
    miro = copy.deepcopy(state)

# for i in range(n):
#     print(*miro[i])
simulation(5)
print(answer)