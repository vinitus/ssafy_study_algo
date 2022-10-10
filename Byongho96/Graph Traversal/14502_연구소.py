# 2204 ms
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

def bfs(starts):
    global mn_infected
    visited = [[0] * M for _ in range(N)]
    q = deque()

    for i, j in starts:
       visited[i][j] = 1
       q.append((i, j))

    cnt = 0
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and  0 <= nj < M and not arr[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))
                cnt += 1                # 전염구간 카운팅
                if cnt >= mn_infected:  # 전염구간이 최소 전염구간 이상이 되었을 경우, 종료
                    return False
    mn_infected = cnt
    return True

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

zeros = []
viruses = []
for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            zeros.append((i, j))
        elif arr[i][j] == 2:
            viruses.append((i, j))

mn_infected = N * M
for comb in combinations(zeros, 3): # 3가지 combinations에 대해서 반복
    for i, j in comb:                   # 벽세우기
        arr[i][j] = 1
    if bfs(viruses):                    # mn_infected가 최솟값으로 업데이트 되었을 경우
        result = len(zeros) - 3 - mn_infected   # result 업데이트
    for i, j in comb:                   # 벽 복원하기
        arr[i][j] = 0

print(result)