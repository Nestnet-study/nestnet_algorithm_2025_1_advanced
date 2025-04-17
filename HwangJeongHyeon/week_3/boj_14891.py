from collections import deque
class Gear:
    def __init__(self,array,left=None,right=None):
        self.lf=None
        self.rt=None
        self.gear=deque(array)
        self.spining=False
    def spin(self,clock=1):
        self.spining=True
        if self.lf and (not self.lf.spining) and self.lf.gear[2]!=self.gear[6]:
            self.lf.spin(-clock)
        if self.rt and (not self.rt.spining) and self.rt.gear[6]!=self.gear[2]:
            self.rt.spin(-clock)
        if clock==1:
            self.gear.appendleft(self.gear.pop())
        else:
            self.gear.append(self.gear.popleft())
        self.spining=False
    def get(self):
        return self.gear[0]
    def display(self): #디버깅 용
        print(""" %d%d%d
%d * %d
 %d%d%d"""%(self.gear[5],self.gear[6],self.gear[7],
     self.gear[4],self.gear[0],
     self.gear[3],self.gear[2],self.gear[1]))
gears=[Gear(list(map(int,input()))),
       Gear(list(map(int,input()))),
       Gear(list(map(int,input()))),
       Gear(list(map(int,input())))]
for i in range(3):
    gears[i].rt=gears[i+1]
    gears[i+1].lf=gears[i]
""" 디버깅 용
for i in range(4):
    gears[i].display()
"""
k=int(input())
for _ in range(k):
    x,d=map(int,input().split())
    x-=1
    gears[x].spin(d)
    """
    디버깅 용
    print('------------')
    for i in range(4):
        gears[i].display()
    """
s=0
for i in range(4):
    s |= gears[i].get()<<i
print(s)
