import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a != b:
        parent[b] = a

t = int(input())
for i in range(1, t+1):
    n = int(input())
    parent = [i for i in range(n)]

    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        union(parent, a, b)

    m = int(input())
    answer = [0] * m

    for j in range(m):
        s, d = map(int, input().split())
        if find(parent, s) == find(parent, d):
            answer[j] = 1
            
    print("Scenario {}:".format(i))
    for j in range(m):
        print(answer[j])
    print()