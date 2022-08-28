import sys
sys.stdin = open('input.txt')

def dfs(k, lst, ans):
    if k == M:
        print(' '.join(map(str, ans)))
        return

    for num in lst:
        dfs(k + 1, lst, ans + [num])

N, M = map(int, input().split())

lst = [i + 1 for i in range(N)]

dfs(0, lst, [])