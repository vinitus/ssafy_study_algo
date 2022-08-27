import sys
sys.stdin = open('input.txt')


def dfs(k, lst, ans):
    if k == M:
        print(*ans)
        return

    for ele in lst:
        dfs(k + 1, lst, ans + [ele])

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

dfs(0, lst, [])