import sys
input=sys.stdin.readline
from collections import deque

s=int(input().rstrip())
q=deque([[0,0,1]])
ch=[[0]*1001 for _ in range(1001)]
ch[1][0]=1

while q:
    t,clip,cnt=q.popleft()
    if cnt==s:
        print(t)
        break

    # 화면과 클립보드 각각에는 1000개 이하의 이모티콘이여야 하며, 
    # 방문한 적이 없어야 함 (방문한 적이 있다면 해당 경로까지는 오는 경우는 이미 고려 했을 것.)
    if 0<=cnt<=1000 and 0<=clip<=1000 and not ch[clip][cnt]:
        ch[clip][cnt]=1
        q.append([t+1,cnt,cnt]) # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장  
        q.append([t+1,clip,cnt+clip]) # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
        q.append([t+1,clip,cnt-1]) # 화면에 있는 이모티콘 중 하나를 삭제