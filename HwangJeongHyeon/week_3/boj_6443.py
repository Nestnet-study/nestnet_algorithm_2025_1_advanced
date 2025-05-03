import sys
sys.setrecursionlimit(100001)
print=sys.stdout.write
def backTracking(s=''):
    if left==[0]*26:
        print("%s\n"%s)
        return
    for i in range(26):
        if left[i]>0:
            left[i]-=1
            backTracking(s+chr(ord('a')+i))
            left[i]+=1
T=int(input())
for t in range(T):
    s=input()
    left=[0]*26
    for c in s:
        left[ord(c)-ord('a')]+=1
    backTracking()
