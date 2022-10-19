# 100 ms
from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    visited = [[0] * (M+2) for _ in range(N+2)]
    q = deque()

    visited[i][j] = 1
    q.append((i ,j))
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if arr[ni][nj] == '1' and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                if ni == N and nj == M:
                    return visited[ni][nj]
                q.append((ni, nj))

N, M = map(int, input().split())
arr = ['0' * (M + 2)] + ['0' + input().rstrip() + '0' for _ in range(N)] + ['0' * (M + 2)]

print(bfs(1, 1))