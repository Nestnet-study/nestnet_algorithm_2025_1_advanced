def display():
    for i in range(n):
        if rob[i] == 1:
            print(' [R] ',end = '')
        else:
            print('     ',end = '')
    print()
    for i in range(n):
        print('=<%d>='%dur[i],end='')
    print()
    for i in range(2*n-1,n-1,-1):
        print('=<%d>='%dur[i],end='')
    print()
n,k = map(int,input().split())
dur = list(map(int,input().split()))
rob = [0]*n
level = 1
while 1:
    #print("======== Level : %d ============"%level)
    #print("0 :")
    #display()
    # 컨베이어 벨트 회전
    dur.insert(0,dur.pop(-1))
    rob.pop(-1)
    rob.insert(0,0)
    
    #print("1 :")
    #display()
    
    # 로봇 내리기 1
    if rob[n-1] == 1:
        rob[n-1] = 0
        
    #print("2 :")
    #display()

    # 로봇 스스로 이동
    for i in range(n-2,-1,-1):
        if rob[i] == 1 and rob[i+1] == 0 and dur[i+1] >= 1:
            rob[i] = 0
            rob[i+1] = 1
            dur[i+1] -= 1
            if dur[i+1] == 0 : k -= 1
        
    #print("3 :")
    #display()
    
    # 로봇 내리기 2
    if rob[n-1] == 1:
        rob[n-1] = 0
        
    #print("2 :")
    #display()
    
    # 로봇 올리기
    if rob[0] == 0 and dur[0] > 0:
        rob[0] = 1
        dur[0] -= 1
        if dur[0] == 0 : k -= 1
            
    #print("4 :")
    #display()
    
    # 내구도가 0인 칸의 개수가 k개 이상이라면 과정을 종료
    if k <= 0 : break
    level += 1
print(level)
