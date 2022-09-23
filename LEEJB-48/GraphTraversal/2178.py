import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def traversal():
    queue = deque()
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue.append((0, 0, 1))
    num = 0
    arr[0][0] = '0'
    while queue:
        cur = queue.popleft()
        if cur[0] == N - 1 and cur[1] == M - 1:
            num = cur[2]
            break
        for i in range(4):
            tmp_x = cur[0] + dx[i]
            tmp_y = cur[1] + dy[i]
            if 0 <= tmp_x < N and 0 <= tmp_y < M and arr[tmp_x][tmp_y] == '1':
                arr[tmp_x][tmp_y] = '0'
                queue.append((tmp_x, tmp_y, cur[2] + 1))
    return num


N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]
ans = traversal()
print(ans)
