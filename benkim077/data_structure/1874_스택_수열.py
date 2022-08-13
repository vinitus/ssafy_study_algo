from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


# [2] 0과 4 비교, 4와 3 비교, 3과 6 비교,
n = int(input())
lst = [int(input()) for _ in range(n)]



# [1] O(n^2) 라서 망한 풀이
# n = int(input())
# one_to_n_lst = deque(i + 1 for i in range(n))  # deque(1, 2, 3, 4, 5, 6, 7, 8)
# lst = [int(input()) for _ in range(n)]  # 4, 3, 6, 8, 7, 5, 2, 1
#
# ans_lst = []
# ans = []
#
# for i in range(n):
#     while lst[i] not in ans_lst:
#         ans_lst.append(one_to_n_lst.popleft())
#         ans.append('+')
#     ans_lst.pop()
#     ans.append('-')
#
# print('\n'.join(ans))
