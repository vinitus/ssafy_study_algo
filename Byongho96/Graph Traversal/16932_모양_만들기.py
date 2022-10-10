from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append((i, j))

    cnt = 1
    visited[i][j] = 1
    arr[i][j] = numbering
    while q:
        i, j  = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] and not visited[ni][nj]:
                cnt += 1
                arr[ni][nj] = numbering
                visited[ni][nj] = 1
                q.append((ni, nj))
    ref[numbering] = cnt

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ref = {}

visited = [[0] * M for _ in range(N)]
numbering = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            numbering += 1
# print(arr)
# print(ref)

mx = 0
for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            s = set()
            shape = 1
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] and arr[ni][nj] not in s:
                    s.add(arr[ni][nj])
                    shape += ref[arr[ni][nj]]
            mx = max(mx, shape)

print(mx)