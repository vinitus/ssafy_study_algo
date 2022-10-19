from collections import deque
import sys
input = sys.stdin.readline

# 156ms
def bfs(s, e, path):
    visited = [0] * (N + 1)
    if path:
        for v in path[1:]:
            visited[v] = 1
    visited[s] = [s]

    q = deque()
    q.append(s)
    while q:
        v = q.popleft()
        for w in adjLst[v]:
            if not visited[w]:
                if w == e:
                    return visited[v]
                visited[w] = visited[v] + [w]
                q.append(w)



N, M = map(int, input().split())
adjLst = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjLst[a].append(b)
    adjLst[b].append(a)

for node in range(1, N + 1):
    adjLst[node].sort()

S, E = map(int, input().split())
going_path = bfs(S, E, [])
coming_path = bfs(S, E, going_path)
print(len(going_path) + len(coming_path))