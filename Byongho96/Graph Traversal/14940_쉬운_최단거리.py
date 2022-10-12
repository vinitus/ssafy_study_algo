from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    visited = [[0] * M for _ in range(N)]
    q = deque()

    arr[i][j] = 0
    visited[i][j] = 1
    q.append((i, j))
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] and not visited[ni][nj]:
                arr[ni][nj] = visited[i][j]
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))

    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                arr[i][j] = -1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

si, sj = -1, -1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            si, sj,  = i, j
            break
    if si != -1:
        break

bfs(si, sj)

for row in arr:
    print(*row)