n = int(input())
flowers = []

for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    start = sm * 100 + sd
    end = em * 100 + ed
    flowers.append((start, end))

flowers.sort()

target = 301
end = 1130
count = 0
idx = 0
max_end = 0

while target <= end:
    found = False
    while idx < n and flowers[idx][0] <= target:
        max_end = max(max_end, flowers[idx][1])
        idx += 1
        found = True
    
    if not found:
        count = 0
        break

    count += 1
    target = max_end + 1

print(count)