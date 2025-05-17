class Node:
    def __init__(self):
        self.nodes=[None]*10
        self.end_flag = False
    def push(self, x):
        if self.end_flag:
            return False
        if len(x)==0:
            self.end_flag = True
            return True
        c = x[0]
        other = x[1:]
        t = int(c)
        if self.nodes[t] == None:
            self.nodes[t] = Node()
        return self.nodes[t].push(other)
def main():
    n = int(input())
    a=[]
    for i in range(n):
        a.append(input())
    a.sort()
    tree = Node()
    for i in range(n):
        r = tree.push(a[i])
        if r==False:
            print("NO")
            return;
    print("YES")

T = int(input())
for _ in range(T):
    main()
