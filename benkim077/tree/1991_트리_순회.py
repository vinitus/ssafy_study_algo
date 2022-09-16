import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


def pre_order(node):
    print(node.data, end='')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])


def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != None:
        in_order(tree[node.right_node])


def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end='')


tree = {}

N = int(input())
for _ in range(N):
    data, left, right = input().split()
    if left == '.':
        left = None
    if right == '.':
        right = None    
    tree[data] = Node(data, left, right)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
print()