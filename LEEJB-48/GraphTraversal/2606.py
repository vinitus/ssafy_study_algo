import sys


def input():
    return sys.stdin.readline().rstrip()


def dfs(root):
    stack = [root]
    while stack:
        cur = stack.pop()
        if visited[cur]:
            continue
        visited[cur] = 1
        for i in range(1, N + 1):
            if arr[cur][i] and not visited[i]:
                stack.append(i)
    return None


N = int(input())
arr = [[False] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
k = int(input())

for _ in range(k):
    v1, v2 = map(int, input().split())
    arr[v1][v2] = True
    arr[v2][v1] = True
    
dfs(1)
print(sum(visited) - 1)
