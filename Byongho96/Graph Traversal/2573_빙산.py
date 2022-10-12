from pprint import pprint
from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def melting_bfs(i, j):
    global num_ice
    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1

    q = deque()
    q.append((i, j))
    cnt = 1

    melt = defaultdict(int)
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                    cnt += 1
                elif not arr[ni][nj]:

                    melt[(i, j)] += 1

    # 빙하 녹이기
    if cnt == num_ice:
        for pos, m in melt.items():
            i, j = pos[0], pos[1]
            arr[i][j] = max(0, arr[i][j] - m)
            if not arr[i][j]:
                ice.remove((i, j))
                num_ice -= 1
        return True
    else:
        return False

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

num_ice = 0
ice = []
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            num_ice += 1
            ice.append((i, j))

year = 0
while num_ice:
    if melting_bfs(ice[0][0], ice[0][1]):
        year += 1
    else:
        break

if not num_ice:
    print(0)
else:
    print(year)

# def melting_bfs(i, j):
#     global num_ice
#     visited = [[0] * M for _ in range(N)]
#     visited[i][j] = 1
#
#     q = deque()
#     q.append((i, j))
#     cnt = 1
#
#     melt = defaultdict(int)
#     while q:
#         i, j = q.popleft()
#         for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
#             ni = i + di
#             nj = j + dj
#             if 0 <= ni < N and 0 <= nj < M:
#                 if arr[ni][nj] and not visited[ni][nj]:
#                     visited[ni][nj] = 1
#                     q.append((ni, nj))
#                     cnt += 1
#                 elif not arr[ni][nj]:
#                     melt[(i, j)] += 1
#
#     if cnt == num_ice:
#         for pos, m in melt.items():
#             i, j = pos[0], pos[1]
#             arr[i][j] = max(0, arr[i][j] - m)
#             if not arr[i][j]:
#                 num_ice -= 1
#         return True
#     else:
#         return False
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# num_ice = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j]:
#             num_ice += 1
#
# year = 0
# while num_ice:
#     si, sj = -1, -1
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j]:
#                 si, sj = i, j
#                 break
#         if si != -1:
#             break
#     if melting_bfs(si, sj):
#         year += 1
#     else:
#         break
#
# if not num_ice:
#     print(0)
# else:
#     print(year)