import sys
sys.stdin = open('input.txt')


from collections import deque


def get_startpoint():
    for n in range(N):
        for m in range(M):
            if data[n][m] == 2:
                return (n, m)



def bfs():
    q = deque()
    q.append((si, sj))
    vsted[si][sj] = 0

    while q:
        i, j = q.popleft()
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not vsted[ni][nj] and data[ni][nj] == 1:
                q.append((ni,nj))
                vsted[ni][nj] = vsted[i][j] + 1


N, M = map(int, input().split())    # 세로, 가로 크기
data = [list(map(int, input().split())) for _ in range(N)]

si, sj = get_startpoint()
vsted = [[0] * M for _ in range(N)]
bfs()

for n in range(N):
    for m in range(M):
        if data[n][m] == 1 and not vsted[n][m]:
            vsted[n][m] = -1

# 출력
for row in vsted:
    print(*row)