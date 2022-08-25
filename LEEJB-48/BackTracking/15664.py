import sys


def input():
    return sys.stdin.readline().rstrip()


dic = {}


def backtracking(i, ret):
    if len(ret) == M:
        dic[tuple(ret)] = True
        return None
    if i == N:
        return None

    backtracking(i + 1, ret + [nums[i]])
    backtracking(i + 1, ret)


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
backtracking(0, [])
for key in dic.keys():
    print(*key)
