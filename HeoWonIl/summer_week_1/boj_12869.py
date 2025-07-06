from itertools import permutations
import sys
input=sys.stdin.readline

n=int(input().rstrip())
arr=list(map(int,input().rstrip().split()))
arr+=[0]*(3-len(arr))

d={}

def dfs(x,y,z):
    global ans
    if (x,y,z) in d:
        return d[(x,y,z)]
    if (x,y,z)==(0,0,0):
        return 0

    ans = int(1e9)
    for a,b,c in permutations([9,3,1],3):
        ans=min(ans,dfs(max(x-a,0),max(y-b,0),max(z-c,0))+1)
    d[(x,y,z)]=ans

    return ans

print(dfs(*arr))