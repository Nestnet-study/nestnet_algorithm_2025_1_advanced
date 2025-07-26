# union find?
import sys
input=lambda : sys.stdin.readline().rstrip()
print=lambda x: sys.stdout.write(str(x)+'\n')
def union(x,y):
    mem[find(x)]=find(y)
def find(x):
    if x==mem[x]:
        return x
    else:
        mem[x]=find(mem[x])
        return mem[x]
T=int(input())
for c in range(T):
    n=int(input())
    k=int(input())
    mem=list(range(n)) #[0,1,2,3,...,n-1]
    for i in range(k):
        a,b=map(int,input().split())
        union(a,b)
    m=int(input())
    print("Scenario %d:"%(c+1))
    for i in range(m):
        a,b=map(int,input().split())
        if find(a)==find(b):
            print(1)
        else:
            print(0)
    print('')
