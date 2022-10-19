from pprint import pprint
from collections import deque
import sys
input = sys.stdin.readline


# 단순히 2차원 배열로 풂면, 시물레이션에 정확히 이루어지지 않음
# 하나를 먼저 돌리고, 그 다음에 visited조건에 맞추어 다음 것
# fire는 여러개가 주어질 수 있음

def bfs_fire(fire_lst):
    q = deque()

    for i, j in fire_lst:
        f_visited[i][j] = 1
        q.append((i, j))

    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and not f_visited[ni][nj] and arr[ni][nj] != '#':
                f_visited[ni][nj] = f_visited[i][j] + 1
                q.append((ni, nj))

def bfs_jihun(i, j):
    q = deque()

    j_visited[i][j] = 1
    q.append((i, j))

    while q:
        i, j = q.popleft()
        if i in (0, N-1) or j in (0, M-1):
            return j_visited[i][j]
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and not j_visited[ni][nj] and arr[ni][nj] != '#':
                if not f_visited[ni][nj] or j_visited[i][j] < f_visited[ni][nj] - 1: # WARNING: 불이 안났을 수도 있음!!!!
                    j_visited[ni][nj] = j_visited[i][j] + 1
                    q.append((ni, nj))
    return False

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

ji, jj = -1, -1
fire_lst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'J':
            ji, jj = i, j
        elif arr[i][j] == 'F':
            fire_lst.append((i, j))

f_visited = [[0] * M for _ in range(N)]
bfs_fire(fire_lst)
# print(f_visited)
j_visited = [[0] * M for _ in range(N)]
result = bfs_jihun(ji, jj)

if result:
    print(result)
else:
    print('IMPOSSIBLE')