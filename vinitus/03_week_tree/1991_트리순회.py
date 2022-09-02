import sys
def input():
    return sys.stdin.readline().rstrip()

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def forward(node):
    print(node.data, end="")
    if node.left:
        forward(tree[node.left])
    if node.right:
        forward(tree[node.right])

def middle(node):
    if node.left:
        middle(tree[node.left])
    print(node.data, end="")
    if node.right:
        middle(tree[node.right])

def back(node):
    if node.left:
        back(tree[node.left])
    if node.right:
        back(tree[node.right])
    print(node.data, end="")

N = int(input())
tree = {}
for _ in range(N):
    a,b,c = input().split()
    if b == '.':
        b = None
    if c == '.':
        c = None
    tree[a] = Node(a,b,c)


forward(tree['A'])
print()
middle(tree['A'])
print()
back(tree['A'])