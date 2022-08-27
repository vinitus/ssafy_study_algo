import sys
sys.stdin = open('input.txt')


def dfs(k, lst, prev, ans):
    if k == M:
        print(*ans)
        return

    for ele in lst:
        if ele >= prev:
            dfs(k + 1, lst, ele, ans + [ele])

N, M = map(int, input().split())

lst = sorted(list(map(int, input().split())))

dfs(0, lst, 0, [])