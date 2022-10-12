from collections import deque
from pprint import pprint

def bfs(starts):
    visited = [[[0] * M for _ in range(N)] for _ in range(H)]
    q = deque()

    for start in starts:
        h, i, j = start
        visited[h][i][j] = 1
    q.extend(starts)

    days = 1
    while q:
        h, i, j = q.popleft()
        for dh, di, dj in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)):
            nh = h + dh
            ni = i + di
            nj = j + dj
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and not visited[nh][ni][nj] and arr[nh][ni][nj] != -1:
                q.append((nh, ni, nj))
                visited[nh][ni][nj] = visited[h][i][j] + 1
                days = visited[nh][ni][nj]
                arr[nh][ni][nj] = 1

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if not arr[h][i][j]:
                    return -1

    return days - 1


M, N, H = map(int, input().split())

arr = [0] * H
for i in range(H):
    arr[i] = [list(map(int, input().split())) for _ in range(N)]

starts = []
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                starts.append((h, i, j))

result = bfs(starts)

print(result)