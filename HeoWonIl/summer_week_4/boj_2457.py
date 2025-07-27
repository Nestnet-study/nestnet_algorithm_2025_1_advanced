import sys
input=sys.stdin.readline

arr=[]
n=int(input().rstrip())
for _ in range(n):
    sm,sd,em,ed=map(int,input().rstrip().split())
    arr.append([sm*100+sd,em*100+ed])
arr.sort()

ld=301
ans=0

while(arr):
    if(ld>=1201 or arr[0][0]>ld):
        break
    tmp_ld=-1

    for _ in range(len(arr)):
        if(arr[0][0]<=ld):
            if(tmp_ld<=arr[0][1]):
                tmp_ld=arr[0][1]

            arr.remove(arr[0])
        else:
            break

    ld=tmp_ld
    ans+=1

if ld<1201:
    print(0)
else:
    print(ans)