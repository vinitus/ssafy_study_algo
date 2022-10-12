from collections import deque
import sys
input = sys.stdin.readline

# 96ms
def bfs(i, j):
    visited = [[0] * M for _ in range(N)]
    q = deque()

    visited[i][j] = 1
    q.append((i, j))

    sword = N * M
    princess = N * M
    while q:
        i, j = q.popleft()
        if arr[i][j] == 2:
            sword = visited[i][j]-1 + N-1-i + M-1-j
        if i == N - 1 and j == M - 1:
            princess = visited[i][j] - 1
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] != 1:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))
    # 검과 공주 둘다한테 못갈 수도 있음!!
    return min(sword, princess)


N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = bfs(0, 0)
if result == M*N:
    print('Fail')
elif result <= T:
    print(result)
else:
    print('Fail')

