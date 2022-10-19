from pprint import pprint
from collections import deque
import sys
input = sys.stdin.readline

def bfs(k, i, j):
    visited = [[[0] * M for _ in range(N)] for _ in range(2)]
    q = deque()

    visited[k][i][j] = 1
    q.append((k, i, j))

    while q:
        k, i, j = q.popleft()
        if i == N-1 and j == M-1:
            return visited[k][i][j]
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if not arr[ni][nj] and not visited[k][ni][nj]:         # 벽이 없다면
                    q.append((k, ni, nj))
                    visited[k][ni][nj] = visited[k][i][j] + 1
                if not k and arr[ni][nj] and not visited[k+1][ni][nj]:   # 벽이 있고, 부술 수 있다면
                    q.append((k+1, ni, nj))
                    visited[k+1][ni][nj] = visited[k][i][j] + 1
    return -1

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

print(bfs(0, 0, 0))