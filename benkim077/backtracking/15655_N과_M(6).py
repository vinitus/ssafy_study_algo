import sys
sys.stdin = open('input.txt')


def dfs(k, lst, vsted, prev, ans):
    if k == M:
        print(*ans)
        return

    for ele in lst:
        if ele[0] > prev and not vsted[ele[1]]:
            vsted[ele[1]] = True
            dfs(k + 1, lst, vsted, ele[0], ans + [ele[0]])
            vsted[ele[1]] = False


N, M = map(int, input().split())
lst = sorted([(v, i) for (i, v) in enumerate(map(int, input().split()))])

vsted = [False] * N

dfs(0, lst, vsted, 0, [])