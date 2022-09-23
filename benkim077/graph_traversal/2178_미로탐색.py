from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    vsted[si][sj] = 1

    while q:
        i, j = q.popleft()
        for (di, dj) in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N + 1 and 0 <= nj < M + 1 and map_data[ni][nj] != 0 and not vsted[ni][nj]:
                q.append((ni, nj))
                vsted[ni][nj] = vsted[i][j] + 1
    

N, M = map(int, input().split())    # 세로, 가로 길이
map_data = [[0] * (M + 1)] + [[0] + list(map(int, input())) for _ in range(N)]

vsted = [[0] * (M + 1) for _ in range(N + 1)]

bfs(1, 1)
print(vsted[N][M])