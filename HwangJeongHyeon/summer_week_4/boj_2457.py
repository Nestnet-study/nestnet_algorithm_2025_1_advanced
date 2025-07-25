import heapq
def m2d(m,d):
    res=d
    if m>1:res+=31
    if m>2:res+=28
    if m>3:res+=31
    if m>4:res+=30
    if m>5:res+=31
    if m>6:res+=30
    if m>7:res+=31
    if m>8:res+=31
    if m>9:res+=30
    if m>10:res+=31
    if m>11:res+=30
    return res
n=int(input())
pq=[]
for i in range(n):
    m1,d1,m2,d2=map(int,input().split())
    heapq.heappush(pq,(m2d(m1,d1),m2d(m2,d2)-1))
ma,mb=m2d(3,1)-1,m2d(3,1)-1
c=m2d(11,30)
count=0
flag=False
for i in range(n):
    a,b=heapq.heappop(pq)
    #print(a,b)
    if ma+1<a:#더이상 안됨
        #print("더이상",ma,mb)
        if mb+1<a:break
        ma=mb
        #print("ma=%d count+=1"%ma)
        count+=1
    mb=max(mb,b)
    #print("mb=%d"%mb)
    if mb>=c:
        flag=True
        count+=1
        break
if flag:
    print(count)
else:
    print(0)
        
