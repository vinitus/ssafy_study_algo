import sys
sys.setrecursionlimit(10**8)
def input():
    return sys.stdin.readline().rstrip()

def check(idx):
    return 0<=idx<N

class Node:
    def __init__(self,data,up=None,left=None,right=None):
        self.data = data
        self.up = up
        self.left = left
        self.right = right

def upup(node):
    return node.up

lst = []
a = input()

while a != "":
    lst.append(int(a))
    a = input()

N = len(lst)


tree = {lst[0]:Node(lst[0])}
for i in range(1,N):
    if check(i-1) and lst[i-1] > lst[i]:
        tree[lst[i-1]].left = lst[i]
        tree[lst[i]] = Node(lst[i])
        tree[lst[i]].up = lst[i-1]
    else:
        idx = i-1
        while tree[lst[idx]].up is not None:
            if tree[lst[idx]].right is None and (tree[lst[idx]].left is not None or tree[lst[idx]].up > lst[i]):
                tree[lst[idx]].right = lst[i]
                tree[lst[i]] = Node(lst[i],up=lst[idx])
                break
            idx -= 1
        else:
            tree[lst[0]].right = lst[i]
            tree[lst[i]] = Node(lst[i], up=lst[0])

def back(node):
    if node.left:
        back(tree[node.left])
    if node.right:
        back(tree[node.right])
    print(node.data)

back(tree[lst[0]])