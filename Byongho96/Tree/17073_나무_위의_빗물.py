# 1880ms
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    visited = [0] * (N+1)
    q = deque()

    visited[start] = 1
    q.append(start)

    while q:
        v = q.popleft()
        if len(adjLst[v]) == 1 and v != 1:
            leaves.append(visited[v])
        for w in adjLst[v]:
            if not visited[w]:
                q.append(w)
                if v == 1:
                    visited[w] = visited[v] / (len(adjLst[v]))
                else:
                    visited[w] = visited[v] / (len(adjLst[v])-1)

N, W = map(int, input().split())
adjLst = [[] for _ in range(N + 1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adjLst[a].append(b)
    adjLst[b].append(a)

leaves = []

bfs(1)
result = sum([W*x for x in leaves])/len(leaves)
print(result)