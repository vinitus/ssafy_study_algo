# 912ms
from collections import deque
import sys
input = sys.stdin.readline

N, R = map(int, input().split())
adjLst = [[] for _ in range(N + 1)]
for _ in range(N-1):
    a, b, d = map(int, input().split())
    adjLst[a].append((b, d))
    adjLst[b].append((a, d))

def bfs(rt, dis):
    distance = [-1] * (N + 1)
    q = deque()

    distance[rt] = dis
    q.append(rt)

    trunk, branch = 0, 0
    flag = 0

    if len(adjLst[rt]) > 1:
        flag = 1

    while q:
        v = q.popleft()
        if not flag and len(adjLst[v]) > 2:
            trunk = distance[v]
            flag = 1
        for w in adjLst[v]:
            if distance[w[0]] == -1:
                q.append(w[0])
                distance[w[0]] = distance[v] + w[1]

    if not flag:
        trunk = max(distance)
    branch = max(distance) - trunk
    return trunk, branch

trunk, branch = bfs(R, 0)
print(trunk, branch)