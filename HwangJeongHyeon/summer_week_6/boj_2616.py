'''
[왼쪽][가운데][오른쪽]
dp1[i] : 0~i범위에서 시작하는 길이가 L인 가장 큰 합
dp2[i] : i~n-m범위에서 시작하는 길이가 L인 가장 큰 합
가운데의 위치를 조정하면서 dp1 + 가운데 + dp2

7 2
0 1 2 3 4 5 6

16
[37, 53, 13, 67, 13, 14, 9, 58, 61, 83, 60, 53, 43, 3, 49, 75]
2
출력 : 392
정답 : 386
16
37 53 13 67 13 14 9 58 61 83 60 53 43 3 49 75
2
'''
def main():
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    print(fn(n,a,m))
def fn(n,a,m):
    res=0 # 결과 값
    x=sum(a[:m])
    s=[x]
    for i in range(1,n-m+1):
        x-=a[i-1]
        x+=a[i+m-1]
        s.append(x)
    
    # s의 크기 : n-m+1 | s[i] : a[i]부터 연속하는 m개의 합
    dp1=[0]*n;dp2=[0]*n
    x=s[0]
    for i in range(n-m+1):
        x=max(x,s[i])
        dp1[i]=x
    x=s[-1]
    for i in range(n-m,-1,-1):
        x=max(x,s[i])
        dp2[i]=x

    for i in range(m,n-2*m+1): #가운데
        #print(i)
        res=max(res,dp1[i-m]+s[i]+dp2[i+m])
    #print(dp1,dp2)
    return res
main()
