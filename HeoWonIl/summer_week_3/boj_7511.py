import sys
input=sys.stdin.readline

def find(x):
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

def uni(x,y):
    if x==y:
        return
    x=find(x)
    y=find(y)
    p[x]=y

for t in range(1,int(input().rstrip())+1):
    print(f'Scenario {t}:')
    n=int(input().rstrip())
    p=[i for i in range(n)]
    for _ in range(int(input().rstrip())):
        a,b=map(int,input().rstrip().split())
        uni(a,b)
    for _ in range(int(input().rstrip())):
        a,b=map(int,input().rstrip().split())
        print(1 if find(a)==find(b) else 0)
    print()