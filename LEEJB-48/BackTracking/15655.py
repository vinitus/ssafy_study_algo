import sys


def input():
    return sys.stdin.readline().rstrip()


def backtracking(i, ret):
    if len(ret) == M:
        print(*ret)
        return None
    if i == N:
        return None
    backtracking(i + 1, ret + [arr[i]])
    backtracking(i + 1, ret)


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
backtracking(0, [])
