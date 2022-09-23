import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")


#############################
def wall_move():
    global arr
    tmp_arr = []
    for r, c in arr:
        if r + 1 < 8:
            tmp_arr.append((r + 1, c))
    arr = tmp_arr
    return None


dx = [0, 0, 0, 1, -1, 1, 1, -1, - 1]
dy = [0, 1, -1, 0, 0, 1, -1, 1, -1]


def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    queue.append(0)
    while queue and arr:
        cur = queue.popleft()
        if not cur:
            if queue:
                if arr:
                    wall_move()
                    queue.append(0)
                    continue
                else:
                    return 1
            else:
                return 0
        if cur in arr:
            continue
        for i in range(9):
            tmp_x = cur[0] + dx[i]
            tmp_y = cur[1] + dy[i]
            if 0 <= tmp_x < 8 and 0 <= tmp_y < 8 and not (tmp_x, tmp_y) in arr:
                queue.append((tmp_x, tmp_y))
    return 1


arr = [list(input()) for _ in range(8)]
arr = [(r, c) for r in range(8) for c in range(8) if arr[r][c] == '#']
possible = False
print(bfs(7, 0))
