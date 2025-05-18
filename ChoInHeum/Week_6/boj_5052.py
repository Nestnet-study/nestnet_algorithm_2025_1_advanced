import sys
input = sys.stdin.readline

# Input
t = int(input())
number_list = []

for _ in range(t):
    n = int(input())
    temp = [input().strip() for _ in range(n)]
    number_list.append(temp)

# Main
for numbers in number_list:
    numbers.sort()

for numbers in number_list:
    is_consistent = True
    for i in range(len(numbers) - 1):
        if numbers[i+1].startswith(numbers[i]):
            is_consistent = False
            break
    print("NO" if not is_consistent else "YES")