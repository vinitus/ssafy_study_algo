from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs(start):
    q = deque([start])
    vsted[start] = -1

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not vsted[i]:
                q.append(i)
                vsted[i] = v


N = int(input())    # 노드의 수
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

vsted = [0] * (N + 1)
bfs(1)

for i in range(2, N + 1):
    print(vsted[i])