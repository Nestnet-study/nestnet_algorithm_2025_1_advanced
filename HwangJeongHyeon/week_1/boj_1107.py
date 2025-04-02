"""
일반적으로 접근한다면 숫자를 입력하고 +/-를 통해 이동하는 알고리즘이겠지만,
이 경우 시간초과가 될 수 있다.
하지만 역으로 생각해보면
원하는 값인 N에서 +/-로 이동한 뒤 그 값이 가능한 값인지 검사하는 것이다.
+방향과 -방향으로 쭉 가는 a와 b로 숫자를 표현하다.
어떤 값을 받았을 때 가능한 값인지 확인하는 함수 fn을 만든다.
모든 경우의 수에서 최소값을 구한다.
"""
inf = 2**31-1
def fn(n):
    if n<0 or n>1000000:return False
    if n==100:return True
    if n==0 and 0 in broken:return False
    while n!=0:
        r=n%10
        n//=10
        if r in broken:
            return False
    return True
# 입력
n=int(input())
m=int(input())
if m!=0:
    broken=list(map(int,input().split()))
else:
    broken=[]
r=inf
for i in range(1000001):
    a=n+i
    b=n-i
    if fn(a):
        x=a-n
        if a!=100:x+=len(str(a))
        r=min(r,x)
    if fn(b):
        x=n-b
        if b!=100:x+=len(str(b))
        r=min(r,x)
print(r)
