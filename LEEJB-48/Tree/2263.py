import sys
def input():
    return sys.stdin.readline().rstrip()

sys.setrecursionlimit(100000)
#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################

def restore(parent, direction, in_l, in_r, pos_l, pos_r):
    """if parent == 0:
        root = postorder[pos_r-1]
        print(root, end=' ')
        in_index = inorder.index(root)
        if in_index > in_l:
            restore(root,'left',in_l,in_index,pos_l, pos_l + in_index - in_l)
        if in_index + 1 < in_r:
            restore(root,'right',in_index+1,in_r,pos_r - in_r + in_index, pos_r - 1)

    else:
        if direction == 'left':
            if in_r - in_l == 1:
                print(inorder[in_l], end=' ')
                return None
            else:
                root = postorder[pos_r - 1]
                print(root, end=' ')
                in_index = inorder.index(root)
                if in_index > in_l:
                    restore(root, 'left', in_l, in_index, pos_l, pos_l + in_index - in_l)
                if in_index + 1 < in_r:
                    restore(root, 'right', in_index + 1, in_r, pos_r - in_r + in_index, pos_r - 1)

        else:
            if in_r - in_l == 1:
                print(inorder[in_l], end=' ')
                return None
            else:
                root = postorder[pos_r - 1]
                print(root, end=' ')
                in_index = inorder.index(root)
                if in_index > in_l:
                    restore(root, 'left', in_l, in_index, pos_l, pos_l + in_index - in_l)
                if in_index + 1 < in_r:
                    restore(root, 'right', in_index + 1, in_r, pos_r - in_r + in_index, pos_r - 1)
    """
    if in_r - in_l == 1:
        print(inorder[in_l], end=' ')
        return None
    root = postorder[pos_r - 1]
    print(root, end=' ')
    in_index = inorder.index(root)
    if in_index > in_l:
        restore(root, 'left', in_l, in_index, pos_l, pos_l + in_index - in_l)
    if in_index + 1 < in_r:
        restore(root, 'right', in_index + 1, in_r, pos_r - in_r + in_index, pos_r - 1)
N = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
restore(0, 0, 0, len(inorder), 0, len(postorder))
