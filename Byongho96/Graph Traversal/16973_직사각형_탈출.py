from collections import deque
import sys
input = sys.stdin.readline

# 하나씩 다 탐색하면 시간초과
# 벽을 기준으로 <> 연산자로
# 애초에 못갈 곳을 전부 표시

def bfs(i, j):
    visited = [[0] * M for _ in range(N)]
    q = deque()

    visited[i][j] = 1
    q.append((i, j))

    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N - H + 1 and 0 <= nj < M - W + 1 and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                for wi, wj in walls:
                    if ni <= wi <= ni + H - 1 and nj <= wj <= nj + W - 1:
                        break
                else:
                    if ni == Ei - 1 and nj == Ej - 1:
                        return visited[i][j]
                    q.append((ni, nj))
    return -1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
H, W, Si, Sj, Ei, Ej = map(int, input().split())

walls = []
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            walls.append((i, j))

print(bfs(Si-1, Sj-1))