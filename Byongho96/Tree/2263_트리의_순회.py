# https://ku-hug.tistory.com/135?category=978336

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# 304 ms
# postorder와 inorder모두 처음인덱스와 끝인덱스로 넘김
# search하지 않고 index로 찾을 수 있는 리스트 새로 생성
N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

def make_tree(in_start, in_end, post_start, post_end):
    global post_ptr
    if in_end < in_start or post_end < post_start:
        return
    root = postorder[post_end]
    idx = inorder_idx[root]
    size = idx - in_start
    # print('root', root, 'idx', idx, 'size', size)

    print(root, end=' ')

    make_tree(in_start, idx-1, post_start, post_start + size -1)
    make_tree(idx + 1, in_end, post_start + size, post_end -1)

# idx를 구하는 리스트를 미리 형성
inorder_idx = [0] * (N + 1)
for i in range(N):
    inorder_idx[inorder[i]] = i

make_tree(0, N-1, 0, N-1)

#####################################################
# 시간초과

# N = int(input())
# inorder = list(map(int, input().split()))
# postorder = list(map(int, input().split()))
#
# def make_tree(start, end):
#     global post_ptr
#     if end >= start:
#         post_ptr -= 1
#         root = postorder[post_ptr]
#         idx = inorder_idx[root]
#         # print('start:', start, 'end:', end, 'ptr:', post_ptr, 'idx:', idx, 'root:', root)
#         rights = make_tree(idx + 1, end)
#         lefts = make_tree(start, idx - 1)
#         return [root] + lefts + rights
#     return []
#
# # idx를 구하는 리스트를 미리 형성
# inorder_idx = [0] * (N + 1)
# for i in range(N):
#     inorder_idx[inorder[i]] = i

# post_ptr = N
# print(*make_tree(0, N-1))