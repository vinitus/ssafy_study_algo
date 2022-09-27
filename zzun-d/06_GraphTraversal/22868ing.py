from collections import defaultdict
import sys


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
visited = [0]*(N+1)
tree = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

s, e = map(int, input().split())
visited[s] = 1
def dfs(n, t):

    if t == 1 and n == e:
        visited[e] = 1
        return
    elif t == 2 and n == s:
        return

    else:
        tree[n] = sorted(tree[n])
        for i in tree[n]:
            if not visited[i]:
                visited[i] = 1
                dfs(i, t)
                visited[i] = 0


dfs(s, 1)
dfs(s, 2)
print(sum(visited))