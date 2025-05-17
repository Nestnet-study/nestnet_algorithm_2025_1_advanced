import sys
input = sys.stdin.readline

length, width, height = map(int, input().split())
n = int(input())

cubes = [0] * 20
for _ in range(n):
    a, b = map(int, input().split())
    cubes[a] = b

filled_volume = 0
used_count = 0

for i in reversed(range(20)):
    size = 2 ** i
    max_fit = (length // size) * (width // size) * (height // size)
    max_fit -= filled_volume // (size ** 3)
    use = min(cubes[i], max_fit)
    filled_volume += use * (size ** 3)
    used_count += use

if filled_volume == length * width * height:
    print(used_count)
else:
    print(-1)