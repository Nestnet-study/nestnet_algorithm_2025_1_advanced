"""
왔던곳은 다시 못 가고, 아래로만 갈 수 있기에
각 줄은 시작 중간 끝으로 나뉜다.
끝은 다음 줄의 시작으로 연결이 되는 것
이렇게 되면 각 줄의 탐사 시간은
m*(m-1)/2
"""
import sys

sys.setrecursionlimit(2030)
INF=2147483647

input=lambda :sys.stdin.readline().rstrip()
n,m=map(int,input().split())
a=[]
mem1=[]
mem2=[]
for i in range(n):
    a.append(list(map(int,input().split())))
    mem1.append([0]*m)
    mem2.append([0]*m)
mem1[n-1][m-1]=a[n-1][m-1]
mem2[n-1][m-1]=a[n-1][m-1]
for i in range(m-2,-1,-1):
    mem1[n-1][i]=mem1[n-1][i+1]+a[n-1][i]
    mem2[n-1][i]=mem2[n-1][i+1]+a[n-1][i]
#바텀업 방식
for i in range(n-2,-1,-1):
    mem1[i][0]=max(mem1[i+1][0],mem2[i+1][0])+a[i][0]
    mem2[i][m-1]=max(mem1[i+1][m-1],mem2[i+1][m-1])+a[i][m-1]
    for j in range(1,m):
        mem1[i][j]=max(mem1[i][j-1],mem2[i+1][j],mem1[i+1][j])+a[i][j]
        mem2[i][m-j-1]=max(mem2[i][m-j],mem1[i+1][m-j-1],mem2[i+1][m-j-1])+a[i][m-j-1]
print(max(mem1[0][0],mem2[0][0]))

"""
5 5
 10   25   7    8    13
 68   24  -78   63   32 
 12  -69   100 -29  -25 
-16  -22  -57  -33   99
 7   -76  -11   77   15

mem2
 319  309  284  277  269
 242  174  150  228  165
 147  135  204  104  133 <<
-4    2    24   81   114
 12   5    81   92   15
 
mem1
 252  0    0    0    0
 215  239  161  224  256
 8   -61   124  95   133 >>
-4   -17   24   59   158
 12   5    81   92   15

mem[i][j]=max(mem[i][j+1],memOther[i+1][j],mem[i+1][j])+a[i][j]
"""
