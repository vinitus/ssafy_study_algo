import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# 80ms
def backtracking(pre):
    # 종료조건
    if len(perm) == M:
        print(' '.join(map(str, perm)))
    # 가지치기
    # 후보군 콜
    else:
        for i in range(pre, N+1):
            perm.append(i)
            backtracking(i)
            perm.pop()

perm = []
backtracking(1)