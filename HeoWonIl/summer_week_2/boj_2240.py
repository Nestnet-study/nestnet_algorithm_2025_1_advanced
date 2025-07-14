import sys
input=sys.stdin.readline

jadu=[0]
t,w=map(int,input().rstrip().split())
for _ in range(t):
    jadu.append(int(input().rstrip()))

arr=[[0]*(w+1) for _ in range(t+1)]

def jadu_loc(w):
    return 1 if w%2==0 else 2

for t in range(1,t+1):
    arr[t][0]=arr[t-1][0]+int(jadu_loc(0)==jadu[t])

arr[1][1]=int(jadu_loc(1)==jadu[1])
for t in range(2,t+1):
    for w in range(1,w+1):
        arr[t][w]=max(arr[t-1][w-1],arr[t-1][w])+int(jadu_loc(w)==jadu[t])

print(max(arr[t]))