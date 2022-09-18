import sys
def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################


def restore(parent,direction,preor,inor):
    if parent == 0: #맨 처음 시작
        root = preor[0]
        index = inor.index(root)
        if index > 0:
            restore(root, 'left', preor[1:1 + index], inor[:index])
        if preor[1 + index:]:
            restore(root, 'right', preor[1 + index:], inor[index + 1:])
    else:
        if direction == 'left':
            if len(preor) == 1:
                tree[parent][0] = preor[0]
                return None
            else:
                root = preor[0]
                tree[parent][0] = root
                index = inor.index(root)
                if index>0:
                    restore(root, 'left', preor[1:1 + index], inor[:index])
                if preor[1+index:]:
                    restore(root, 'right', preor[1 + index:], inor[index + 1:])
        else:
            if len(preor) == 1:
                tree[parent][1] = preor[0]
                return None
            else:
                root = preor[0]
                tree[parent][1] = root
                index = inor.index(root)

                if index > 0:
                    restore(root, 'left', preor[1:1 + index], inor[:index])
                if preor[1 + index:]:
                    restore(root, 'right', preor[1 + index:], inor[index + 1:])
def postorder(node):
    if tree[node][0]:
        postorder(tree[node][0])
    if tree[node][1]:
        postorder(tree[node][1])
    print(node,end=' ')


T = int(input())
for _ in range(T):
    n = int(input())
    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))
    tree = [[None,None] for i in range(n+1)]
    restore(0,0,preorder,inorder)
    postorder(preorder[0])
    print()