import sys
def input():
    return sys.stdin.readline().rstrip()

class Node:
    def __init__(self,data,up=None,down=[]):
        self.data = data
        self.up = up
        self.down = down

llst = []
lst = []
while True:
    tmp = input().split('  ')
    if tmp == ['-1 -1']:
        break
    elif tmp == ['']:
        continue
    elif '0 0' in tmp:
        tmp.pop()
        for i in tmp:
            lst.append(list(map(int, i.split())))
        llst.append(lst)
        lst = []
    else:
        for i in tmp:
            lst.append(list(map(int, i.split())))

for t in range(1,len(llst)+1):
    lst = llst[t-1][:]
    node = {}
    if len(lst) <= 0:
        print()
    for i in lst:
        a,b = i[0],i[1]
        if a not in node:
            node[a] = Node(a,down=[b])
        else:
            node[a].down.append(b)
        if b not in node:
            node[b] = Node(b,up=a)
        elif node[b].up:
            print(f'{t} not')
            break
        else:
            node[b].up = a
    else:
        tree = []
