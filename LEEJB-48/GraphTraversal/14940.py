import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(i, j):
    queue = deque()
    cnt = 0
    queue.append((i, j))
    matrix[i][j] = 1000000
    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            for k in range(4):
                tmp_x = cur[0] + dx[k]
                tmp_y = cur[1] + dy[k]
                if 0 <= tmp_x < n and 0 <= tmp_y < m:
                    if arr[tmp_x][tmp_y] and not matrix[tmp_x][tmp_y]:
                        matrix[tmp_x][tmp_y] = cnt + 1
                        queue.append((tmp_x, tmp_y))
        cnt += 1


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            posi = (i, j)
            break
    else:
        continue
    break
bfs(posi[0], posi[1])
for i in range(n):
    for j in range(m):
        if arr[i][j] and not matrix[i][j]:
            matrix[i][j] = -1

matrix[posi[0]][posi[1]] = 0
for lis in matrix:
    print(*lis)
