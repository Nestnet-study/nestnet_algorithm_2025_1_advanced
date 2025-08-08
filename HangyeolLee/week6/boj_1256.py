from math import comb
n,m,k = map(int,input().split())

answer = ""

if k > comb(n+m,n):
    print(-1)
    exit()

for i in range(n+m):
    if comb(n+m-1, m) >= k:
        answer += "a"        
        n-=1
    else:
        answer += "z"
        k -= comb(n+m-1, m)
        m-=1

print(answer)
