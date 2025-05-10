n,s=map(int,input().split())
a=list(map(int,input().split()))

i,j=0,0
g=0
ct=n+1
while j<=n:
    if g>=s:
        ct=min(ct,j-i)
        if ct==0:break;
        g-=a[i]
        i+=1
    else:
        if j>=n:break;
        g+=a[j]
        j+=1
if ct==n+1:
    print(0)
else:
    print(ct)
