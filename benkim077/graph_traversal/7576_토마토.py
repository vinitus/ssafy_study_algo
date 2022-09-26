# 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다.
# 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

# 예제입력
# 6 4
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1
# 에제출력
# 8

# 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
from collections import deque


def bfs():
    global dq
    for si, sj in dq:
        vsted[si][sj] = True
    
    while dq:
        i, j = dq.popleft()
        for (di, dj) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not vsted[ni][nj] and data[ni][nj] == 0:
                dq.append((ni, nj))
                vsted[ni][nj] = True
                data[ni][nj] = data[i][j] + 1


def check_ans():
    mx = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                return -1
            else:
                mx = max(mx, data[i][j] - 1)
    else:
        return mx


M, N = map(int, input().split())    # M: 가로, N : 세로
data = [list(map(int, input().split())) for _ in range(N)]

dq = deque()
for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            dq.append((i, j))

vsted = [[False] * M for _ in range(N)]
bfs()

ans = check_ans()
print(ans)