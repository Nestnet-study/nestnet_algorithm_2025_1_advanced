"""
1. k개 꽉 찰 때 까지 집어넣기
2. 꽉차면 우선 순위 큐에서 빼기 끝나는 시간이 빠른 같으면 다 + k가 클수록 우선순위 A
"""
from heapq import *
pq = []
n,k=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
time=0
counter=[]
res=0
resct=1
for i in range(k):
    heappush(counter,i)
for i in range(n+1): # 마지막 i==n은 남아있는 것 빼내는 용도
    if len(pq)>=k or (i==n and len(pq)>0):
        # 시간이 흐르고...
        # 시간 확인용 미리 하나 빼기
        time,c,d=heappop(pq)
        heappush(counter,-c)
        res+=resct*d
        resct+=1
        while len(pq):
            t,c,d=heappop(pq)
            if t!=time and i!=n: # 동시에 끝나는 것이 아니면 다시 넣고 다음으로
                heappush(pq,[t,c,d])
                break
            heappush(counter,-c)
            res+=resct*d
            resct+=1
    if i==n:break
    # 빈 공간이 남았으면
    c=heappop(counter)
    heappush(pq,[a[i][1]+time,-c,a[i][0]])
print(res)
"""
12345678901234567890124567890
123123456789012341234567890
12341123456712345123
12345123451234567
"""











