import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


M, N, H = map(int, input().split())

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    queue = deque()
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if arr[h][n][m] == 1:
                    queue.append((h, n, m))
    cnt = 0
    queue.append(0)
    while queue:
        cur = queue.popleft()
        if not cur:
            if queue:
                queue.append(0)
                cnt += 1
                continue
            else:
                break
        for i in range(6):
            tmp_h = cur[0] + dz[i]
            tmp_r = cur[1] + dx[i]
            tmp_c = cur[2] + dy[i]
            if 0 <= tmp_h < H and 0 <= tmp_r < N and 0 <= tmp_c < M and not arr[tmp_h][tmp_r][tmp_c]:
                arr[tmp_h][tmp_r][tmp_c] = 1
                queue.append((tmp_h, tmp_r, tmp_c))

    return cnt


def is_all_ik():
    for h in range(H):
        for lis in arr[h]:
            if not all(lis):
                return 0
    return 1


# 높이,N,M
# arr[h] 기준으로는 [row][column] , row = N , column = M
arr = [[list(map(int, input().split())) for i in range(N)] for _ in range(H)]
ans = bfs()
if is_all_ik():
    print(ans)
else:
    print(-1)
