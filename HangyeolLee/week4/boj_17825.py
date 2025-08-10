import sys
input = sys.stdin.readline

dice = list(map(int, input().split())) 

next_node = [0] * 34
score     = [0] * 34

for i in range(0, 20):
    next_node[i] = i + 1
next_node[20] = 32              
for idx, val in enumerate(range(2, 41, 2), start=1):
    score[idx] = val
score[32] = 0

special_next = {
    5: 21,   
    10:28,   
    15:30,   
}

score[21] = 13; next_node[21] = 22
score[22] = 16; next_node[22] = 23
score[23] = 19; next_node[23] = 24

score[24] = 25; next_node[24] = 25
score[25] = 30; next_node[25] = 26
score[26] = 35; next_node[26] = 20

score[28] = 22; next_node[28] = 29
score[29] = 24; next_node[29] = 24    

score[30] = 28; next_node[30] = 31
score[31] = 27; next_node[31] = 33
score[33] = 26; next_node[33] = 24    

pos = [0] * 4     # 각 말의 현재 노드 idx
finished = [False] * 4 # 도착 여부
max_score = 0

def move(start, steps):
    cur = start
    if cur == 32:
        return 32
    for i in range(steps):
        if cur == 32:
            break
        if i == 0 and cur in special_next:
            cur = special_next[cur]
        else:
            cur = next_node[cur]
    return cur

def is_conflict(i, new):
    if new == 32:
        return False
    for j in range(4):
        if j == i or finished[j]:
            continue
        if pos[j] == new:
            return True
    return False

def dfs(turn, total):
    global max_score
    if turn == 10:
        max_score = max(max_score, total)
        return

    for i in range(4):
        if finished[i]:
            continue
        cur = pos[i]
        new = move(cur, dice[turn])
        if is_conflict(i, new):
            continue

        prev_finish = finished[i]
        pos[i] = new
        if new == 32:
            finished[i] = True

        dfs(turn + 1, total + score[new])

        pos[i] = cur
        finished[i] = prev_finish

dfs(0, 0)
print(max_score)