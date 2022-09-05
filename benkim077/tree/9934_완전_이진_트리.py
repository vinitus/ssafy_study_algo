# Perfect Binary Tree의 깊이가 K 일 때, 노드의 갯수는 2^K - 1개이다.
# PBT 루트의 자식 노드는 깊이가 K - 1 인, PBT이다. 그러므로 노드의 갯수는 2^(K -1) - 1개이다.
# 그러므로 입력으로 주어지는 K(깊이)와 노드 목록을 > 부모 노드, 좌측 트리, 우측 트리로 구분할 수 있다.
# 이를 재귀로 구현해보자.
# K(깊이)가 주어졌으므로, 길이가 K인 리스트를 만들어서 보관해보자.
import sys
sys.stdin = open('input.txt')

# tree의 깊이 k
def recur_f(tree, k):
    global K
    if k == 1:  # 깊이가 1이면 종료
        ans_lst[K - k].append(tree[0])
        return
    else:
        ans_lst[K - k].append(tree[len(tree)//2])
        recur_f(tree[:len(tree)//2], k - 1)
        recur_f(tree[len(tree)//2 + 1:], k - 1)


K = int(input())
data = list(map(int, input().split()))
ans_lst = [[] for _ in range(K)]

recur_f(data, K)

for i in range(K):
    print(*ans_lst[i])