import sys
input = sys.stdin.readline

n, l = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]

answer = 0

# 가로 검사
for i in range(n):
    path = [0] * n
    check = 1
    for j in range(n - 1):
        height_diff = Map[i][j] - Map[i][j + 1]

        if height_diff == 0:
            continue
        # 내려가는 경사로
        elif height_diff == 1:
            for k in range(j + 1, j + 1 + l):
                if k >= n or Map[i][k] != Map[i][j + 1] or path[k]:
                    check = 0
                    break
            if check:
                for k in range(j + 1, j + 1 + l):
                    path[k] = 1
            else:
                break
        # 올라가는 경사로
        elif height_diff == -1:
            for k in range(j, j - l, -1):
                if k < 0 or Map[i][k] != Map[i][j] or path[k]:
                    check = 0
                    break
            if check:
                for k in range(j, j - l, -1):
                    path[k] = 1
            else:
                break
        # 높이 차이 2 이상
        else:
            check = 0
            break
    if check:
        answer += 1

# 세로 검사
for i in range(n):
    path = [0] * n
    check = 1
    for j in range(n - 1):
        height_diff = Map[j][i] - Map[j + 1][i]

        if height_diff == 0:
            continue
        # 내려가는 경사로
        elif height_diff == 1:
            for k in range(j + 1, j + 1 + l):
                if k >= n or Map[k][i] != Map[j + 1][i] or path[k]:
                    check = 0
                    break
            if check:
                for k in range(j + 1, j + 1 + l):
                    path[k] = 1
            else:
                break
        # 올라가는 경사로
        elif height_diff == -1:
            for k in range(j, j - l, -1):
                if k < 0 or Map[k][i] != Map[j][i] or path[k]:
                    check = 0
                    break
            if check:
                for k in range(j, j - l, -1):
                    path[k] = 1
            else:
                break
        # 높이 차이 2 이상
        else:
            check = 0
            break
    if check:
        answer += 1

print(answer)