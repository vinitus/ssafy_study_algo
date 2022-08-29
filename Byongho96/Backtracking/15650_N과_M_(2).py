# 76ms
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

def Backtracking(m, in_perm):
    global result
    # 종료조건
    if m == M + 1:
        result.append(in_perm[1:])
        return
    # 가지치기
    # 후보군
    else:
        for i in range(1, N + 1):
            if (i not in in_perm) and (i > in_perm[-1]):
                Backtracking(m + 1, in_perm + [i])

in_perm = [0]
result = []
Backtracking(1, in_perm)

for ele in result:
    print(*ele)