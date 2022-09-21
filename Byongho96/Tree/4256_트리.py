# 556 ms
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    def make_tree(inorder):
        global pre_ptr
        if inorder:
            pre_ptr += 1
            root = preorder[pre_ptr]
            idx = inorder.index(root)
            left = make_tree(inorder[:idx])
            right = make_tree(inorder[idx + 1:])
            print(root, end=' ')

    pre_ptr = -1
    make_tree(inorder)
    print()