from pprint import pprint
from collections import deque
import sys
input = sys.stdin.readline

d1 = [1, 0, -1, 0, -2, -1, 1, 2, 2, 1, -1, -2]  # 0~3: 네방향 이동, 4~11: 말 이동
d2 = [0, 1, 0, -1, 1, 2, 2, 1, -1, -2, -2, -1]

def bfs(k, i, j):
    visited = [[[0] * M for _ in range(N)] for _ in range(K + 1)]
    for height in range(K+1):
        visited[height][0][0] = 1

    q = deque()
    q.append((k, i, j))

    while q:
        k, i, j = q.popleft()
        if i == N - 1 and j == M - 1:
            return visited[k][i][j] - 1

        for idx in range(4):  # 4가지 이동
            ni = i + d1[idx]
            nj = j + d2[idx]
            if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj] and not visited[k][ni][nj]:
                q.append((k, ni, nj))
                visited[k][ni][nj] = visited[k][i][j] + 1

        if k:                       # 말처럼 움직일 수 있으면
            for idx in range(4, 12):       # 12가지 모두 이동
                ni = i + d1[idx]
                nj = j + d2[idx]
                if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj] and not visited[k-1][ni][nj]:
                    q.append((k-1, ni, nj))
                    visited[k-1][ni][nj] = visited[k][i][j] + 1
    return -1

K = int(input())
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(bfs(K, 0, 0))

# def dfs(i, j, cnt, k):
#     global mn
#     if i == N-1 and j == M-1:
#         mn = min(mn, cnt)
#         return
#     if cnt >= mn:
#         return
#     for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
#         ni = i + di
#         nj = j + dj
#         if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj] and not visited[ni][nj]:
#             visited[ni][nj] = 1
#             dfs(ni, nj, cnt + 1, k)
#             visited[ni][nj] = 0
#     if k:
#         for di, dj in ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)):
#             ni = i + di
#             nj = j + dj
#             if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj] and not visited[ni][nj]:
#                 visited[ni][nj] = 1
#                 dfs(ni, nj, cnt + 1, k-1)
#                 visited[ni][nj] = 0
#
#
# K = int(input())
# M, N = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# visited = [[0] * M for _ in range(N)]
# visited[0][0] = 1
# mn = M * N
# dfs(0, 0, 0, K)
#
# if mn == M * N:
#     print(-1)
# else:
#     print(mn)