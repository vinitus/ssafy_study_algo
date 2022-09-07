import sys
sys.stdin = open('input.txt')

# 전위, 후위 순회를 이용해서
# 트리의 루트 노드를 찾고 좌/우 서브 트리를 찾는 함수
def transfer_post(preorder, inorder):
    # 종료조건
    if len(preorder) == 0:                          # 길이가 0이면 종료
        return
    elif len(preorder) == 1:                        # 길이가 1이면 출력하고 종료
        print(preorder[0], end=' ')
        return
    elif len(preorder) == 2:                        # 길이가 2이면 자리 바꿔서 출력하고 종료
        print(preorder[1], preorder[0], end=' ')
        return

    # 전위 맨 앞 값(루트)의 위치를 중위에서 찾음
    root = inorder.index(preorder[0])
    
    # 중위 순회 왼쪽, 전위 순회 왼쪽을 구해서 다시 재귀
    left_inorder = inorder[0:root]
    left_preorder = preorder[1:1+len(left_inorder)]
    transfer_post(left_preorder, left_inorder)

    # 중위 순회 오른쪽, 전위 순회 왼쪽을 구해서 다시 재귀
    right_inorder = inorder[root+1:]
    right_preorder = preorder[len(left_preorder)+1:]
    transfer_post(right_preorder, right_inorder)

    # 마지막에 전위 맨 앞 값을 호출
    print(preorder[0], end=' ')


T = int(input())

for _ in range(T):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    # 전위 순회, 중위 순회 형태를 넣어 후위 순회를 출력해주는 함수
    transfer_post(preorder, inorder)
    print()


'''
3 6 5 4 8 7 1 2
5 6 8 4 3 1 2 7

6 5 4 8
5 6 8 4
1. 전위 순회의 맨 앞 값은 후위 순회의 맨 뒷값이 된다.
2. 왼쪽 서브트리, 오른쪽 서브트리 나눠서 다시 재귀

    6      3

5 8 4 6 2 1 7 3
'''