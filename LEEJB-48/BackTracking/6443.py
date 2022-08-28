import sys


def input():
    return sys.stdin.readline().rstrip()


def backtracking(i, visited, ret):
    if i == length:
        sys.stdout.write(ret + '\n')
        return None
    prev = ''
    for k in range(length):
        if not visited[k]:
            if string[k] == prev:
                continue
            visited[k] = True
            backtracking(i + 1, visited, ret + string[k])
            visited[k] = False
            prev = string[k]


N = int(input())
for _ in range(N):
    string = sorted(input())
    length = len(string)
    backtracking(0, [False] * length, '')
