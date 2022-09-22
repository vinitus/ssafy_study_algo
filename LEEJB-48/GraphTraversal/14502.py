import sys
from itertools import combinations
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")


#############################
def count_safety_zone(array):
    cnt = sum([array[i].count(0) for i in range(len(array))])
    return cnt


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(queue, matrix):
    global min_val
    cnt = 0
    while queue:
        if cnt > min_val:
            return None
        cur = queue.popleft()
        for i in range(4):
            tmp_x = cur[0] + dx[i]
            tmp_y = cur[1] + dy[i]
            if 0 <= tmp_x < N and 0 <= tmp_y < M and not matrix[tmp_x][tmp_y]:
                matrix[tmp_x][tmp_y] = 2
                queue.append((tmp_x, tmp_y))
                cnt += 1
    min_val = cnt


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque([(i, j) for i in range(N) for j in range(M) if arr[i][j] == 2])
min_val = 64
for w1, w2, w3 in combinations([(i, j) for i in range(N) for j in range(M) if not arr[i][j]], 3):
    arr[w1[0]][w1[1]] = 1
    arr[w2[0]][w2[1]] = 1
    arr[w3[0]][w3[1]] = 1
    bfs(q.copy(), [arr[i][:] for i in range(N)])
    arr[w1[0]][w1[1]] = 0
    arr[w2[0]][w2[1]] = 0
    arr[w3[0]][w3[1]] = 0

print(count_safety_zone(arr) - min_val - 3)
