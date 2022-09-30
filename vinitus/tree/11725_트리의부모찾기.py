import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

node = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)

def dfs():
    visited = [0] * (N+1)
    s = 1
    visited[1] = s
    q = [s]
    idx = s
    while q:
        idx = q.pop()
        for i in node[idx]:
            if not visited[i]:
                visited[i] = idx
                q.append(i)
    for i in range(2, N + 1):
        print(visited[i])

dfs()