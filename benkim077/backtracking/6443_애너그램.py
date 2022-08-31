import sys
sys.stdin = open('input.txt')


def dfs(k, lst, vsted, ans):
    if k == M:
        print(''.join(map(str, ans)))
        return

    prev = 0
    for ele in lst:
        if not vsted[ele[1]]:
            if prev == ele[0]:
                continue
            vsted[ele[1]] = True
            dfs(k + 1, lst, vsted, ans + [ele[0]])
            vsted[ele[1]] = False
            prev = ele[0]


N = int(input())

for _ in range(N):
    lst = sorted([(v, i) for (i, v) in enumerate(input())])
    M = len(lst)
    vsted = [False] * len(lst)

    dfs(0, lst, vsted, [])