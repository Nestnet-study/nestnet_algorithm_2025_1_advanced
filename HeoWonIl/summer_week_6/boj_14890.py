import sys
input=sys.stdin.readline

n,l=map(int,input().rstrip().split())
arr=[list(map(int,input().rstrip().split())) for _ in range(n)]

def sol(a):
    global l
    ch=[0]*len(a)
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            continue

        # -_
        elif a[i]==a[i+1]+1:
            if i+l>=len(a):
                return False
            for j in range(i+1,i+l+1):
                if a[j]!=a[i+1]:
                    return False
                ch[j]=1

        # _-
        elif a[i]==a[i+1]-1:
            if i-l+1<0:
                return False
            for j in range(i-l+1,i+1):
                if ch[j] or a[j]!=a[i]:
                    return False
                # _-의 경우 굳이 방문 체크안해줘도 될 듯
        else:
            return False
    return True

ans=0
for i in range(n):
    ans+=int(sol(arr[i]))
for j in range(n):
    tmp=[]
    for i in range(n):
        tmp.append(arr[i][j])
    ans+=int(sol(tmp))
print(ans)