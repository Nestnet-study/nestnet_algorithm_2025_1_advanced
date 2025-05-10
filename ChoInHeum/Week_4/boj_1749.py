import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

data = [list(map(int, input().split())) for _ in range(N)]

max_sum = -float('inf')

for start_row in range(N):
    temp = [0] * M
    for end_row in range(start_row, N):
        for col in range(M):
            temp[col] += data[end_row][col]
            
        current = temp[0]
        best = temp[0]
        
        for i in range (1, M):
            current = max(temp[i], current + temp[i])
            best = max(best, current)
        
        
        max_sum = max(max_sum, best)
        
        
        
print(max_sum)