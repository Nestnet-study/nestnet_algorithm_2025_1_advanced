# 그래프 구현
class Board:
    tts=0 # TotalScore
    mxtts=0 # MaxTotalScore
    log=[] # (bef,aft,hor)
    horses=[None,None,None,None]# End = None
    start=None
    x=[]
    array=[]
    def __init__(self):
        self.red=None # 빨간색 연결
        self.blue=None # 파란색 연결 기본: None
        self.score=0 # 도착 시 점수
        
        self.horse=[] # 말이 있는지 : [0,1,2,3] pop
    def MoveStart(self,number):
        if self.blue: # 파란 길 우선
            return self.blue.Move(self,number-1)
        elif self.red: # 빨간 길 밖에 없음
            return self.red.Move(self,number-1)
        else: # 둘다 없으면 끝이구나 40에는 의도적으로 둘다 안해놈.
            # 도착 칸에 도착
            Board.horses[self.horse[-1]]=None
            #print((self.score,None,self.horse[-1]))
            Board.log.append((self,None,self.horse.pop()))

            return True
    def Move(self,back,number):
        if number<=0:
            if not len(self.horse):
                # 점수 있는 칸에 도착
                # 점수 업대이트
                Board.tts+=self.score
                Board.mxtts=max(Board.mxtts,Board.tts)
                # 말 업대이트
                self.horse.append(back.horse.pop())
                Board.log.append((back,self,self.horse[-1]))
                #print((back.score,self.score,self.horse[-1]))#
                Board.horses[self.horse[-1]]=self
                return True
            else:
                # 다른 말 있음.
                return False
        # 아직 주사위 만큼 이동을 안 한 상태
        elif self.red:
            return self.red.Move(back,number-1)
        else:
            # 도착 칸에 도착
            hor=back.horse.pop()
            Board.horses[hor]=None
            Board.log.append((back,None,hor))
            #print((back.score,None,hor))
            return True
    def MakeGraph(): #그래프 초기화
        Board.x=[]
        #Start~40,13~19,22~24,28~26,25~35
        #    0~20,21~23,24~25,26~28,29~31
        for i in range(32):
            Board.x.append(Board())
        Board.start=Board.x[0]
        Board.start.horse=[3,2,1,0]
        Board.horses=[Board.start,Board.start,Board.start,Board.start]
        
        for i in range(31):
            Board.x[i].red=Board.x[i+1]
        Board.x[5].blue=Board.x[21] # 10->13
        Board.x[10].blue=Board.x[24]# 20->22
        Board.x[15].blue=Board.x[26]# 30->28
        Board.x[31].red=Board.x[20]
        Board.x[20].red=None  # 40->도착
        Board.x[23].red=Board.x[29] # 19->25
        Board.x[25].red=Board.x[29] # 24->25
        # 점수 배정
        for i in range(21):# 0~20
            Board.x[i].score=i*2
        for i in range(3): # 21~23
            Board.x[i+21].score=13+i*3
        for i in range(2): # 24~25
            Board.x[i+24].score=22+i*2
        for i in range(3): # 26~28
            Board.x[i+26].score=28-i
        for i in range(3): # 29~31
            Board.x[i+29].score=25+i*5
        Board.mxtts=0
        Board.tts=0
        Board.log=[]

            
    def BackTracking():
        if len(Board.log)==0: # 예외처리
            print("Error : 아무것도 없이 백트래킹은 좀;;")
            return False
        bef,aft,hor=Board.log.pop()
        bef.horse.append(hor)
        #print(bef.horse)
        if aft:
            aft.horse.pop() # End = None
            Board.tts-=aft.score
        Board.horses[hor]=bef
        
        #print(bef.horse)
    def Dice(n):# n번째 다이스
        if n==10:return
        for i in range(4):
            #print(n,i)
            if Board.horses[i]==None:continue
            #print(Board.horses[i].horse)
            # i번 말 움직임
            if Board.horses[i]==None or Board.horses[i].horse[-1]!=i:continue
            
            if Board.horses[i].MoveStart(Board.array[n]):
                #print(Board.horses[i].score)
                Board.Dice(n+1);#print(Board.horses[i].score)
                #print("BackTraking() : (n,i):%d,%d"%(n,i))
                #print("before")
                #Board.Test1()
                Board.BackTracking();#print(Board.horses[i].score)
                #print("after")
                #Board.Test1()
    def main(a):
        Board.array=a
        Board.MakeGraph()
        Board.Dice(0)
        print(Board.mxtts)
    def Test1():
        for i in range(len(Board.x)):
            print("[%d] : (%d)"%(i,Board.x[i].score),end='')
            if Board.x[i].red:
                print(", red : (%d)"%Board.x[i].red.score,end='')
            if Board.x[i].blue:
                print(", blue : (%d)"%Board.x[i].blue.score,end='')
            print()
            for j in range(len(Board.x[i].horse)):
                print(Board.x[i].horse[j],end=' ')
            print()

a=list(map(int,input().split()))
Board.main(a)
            
