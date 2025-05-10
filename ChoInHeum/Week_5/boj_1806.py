import sys
input = sys.stdin.readline

N, S = map(int, input().split())
data = list(map(int, input().split()))
result = 0

start = 0
end = 0
total = 0
min_length = N + 1

while end <= N:
    if total >= S:
        min_length = min(min_length, end - start)
        total -= data[start]
        start += 1
    else:
        if end < N:
            total += data[end]
        end += 1
        
        
print(min_length if min_length != N + 1 else 0)