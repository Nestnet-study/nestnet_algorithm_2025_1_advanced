import boj_2616,boj_2616_test,random
def make(n): # n인 테스트 케이스를 만듦
    a=[]
    for i in range(n):
        a.append(random.randrange(1,101))
    m=random.randrange(1,(n-1)//3)
    return a,m
def test(n,x):
    for i in range(x):
        a,m=make(n)
        r1=boj_2616.fn(n,list(a),m)
        r2=boj_2616_test.fn(n,list(a),m)
        if r1==r2:
            print(i,"일치")
        else:
            print(i,"불일치")
            print(n)
            print(a)
            print(m)
            print('출력 :',r1)
            print('정답 :',r2)
            input('계속 진행하기 (Enter)')

'''
14
[10, 7, 20, 8, 9, 6, 18, 3, 12, 20, 15, 8, 9, 9]
3
출력 : 115
정답 : 117

13
[16, 3, 2, 9, 5, 11, 8, 19, 5, 16, 4, 16, 7]
3
출력 : 93
정답 : 95

13
5 10 18 9 12 8 13 2 17 3 9 5 7
3
출력 : 94
정답 : 99

13
[2, 13, 1, 12, 10, 11, 19, 18, 8, 4, 12, 3, 1]
3
출력 : 97
정답 : 98

13
[18, 3, 13, 8, 8, 2, 7, 2, 17, 5, 19, 8, 7]
3
출력 : 93
정답 : 94

13
[9, 6, 13, 4, 17, 2, 17, 1, 13, 14, 1, 19, 16]
3
출력 : 100
정답 : 101

'''
