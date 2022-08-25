import sys


def input():
    return sys.stdin.readline().rstrip()


def backtracking(i, ret):
    if len(ret) == M:
        dic[tuple(ret)] = None
        return None
    for k in range(i, N):
        backtracking(k, ret + [nums[k]])


dic = {}
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
backtracking(0, [])
for key in dic.keys():
    print(*key)
