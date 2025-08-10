def fn(n,a,m):
    x=sum(a[:m])
    s=[x]
    for i in range(1,n-m+1):
        x-=a[i-1]
        x+=a[i+m-1]
        s.append(x)
    big=0
    for i in range(n-m+1):
        for j in range(i+m,n-m+1):
            for k in range(j+m,n-m+1):
                x=s[i]+s[j]+s[k]
                if big<x:big=x
    return big
    #print(big)
def main():
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    print(fn(n,a,m))
