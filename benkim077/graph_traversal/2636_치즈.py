from collections import deque
import sys
sys.stdin = open('input.txt')

# [1] 치즈와 맞닿아있는 부분까지 bfs를 한다.
    # 맞닿아있는 치즈를 2(?)로 전환시킨다.
# [2] 치즈를 없앤다.
    # 치즈의 갯수를 저장해 둔다.
# [3] [1], [2]를 반복한다.
# 마지막 치즈의 갯수와 한 시간 전 치즈의 갯수를 출력
def bfs():
    q = deque(sp_lst)
    for si, sj in sp_lst:
        vsted[si][sj] = True

    while q:
        i, j = q.popleft()
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not vsted[ni][nj] and data[ni][nj] == 1:
                    data[ni][nj] = 2    # 노출된 치즈는 2로 바꿈

            if 0 <= ni < N and 0 <= nj < M and not vsted[ni][nj] and data[ni][nj] == 0:
                q.append((ni, nj))
                vsted[ni][nj] = True
    

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

sp_lst = []
for i in range(N):
    for j in range(M):
        if i == 0 or i == N - 1 or j == 0 or j == M - 1:
            sp_lst.append((i, j))

time = 0
prev = 0
while True:
    vsted = [[False] * M for _ in range(N)]
    bfs() # [1]

    # [2]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == 2:
                cnt += 1
                data[i][j] = 0

    if cnt == 0:    # 지울 치즈가 없는 경우
        break
    
    prev = cnt
    time += 1

# [3]
print(time)
print(prev)