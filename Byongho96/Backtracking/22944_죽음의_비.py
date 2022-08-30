from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j, h, d, ):
    global H
    global D
    U = 0
    visited = [[0] * N for _ in range(N)]
    q = deque()

    q.append((i, j, u))
    visited[i][j] = 1
    H += 1
    while q:
        i, j, u = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:


                if arr[i][j] == 'U':
                    U = D
                elif arr[i][j] == 'E':
                    return visited[i][j] - 1
                print(visited)
                print(f'i: {i}, j: {j}, H: {H}, U:{U}')
                if U > 0:
                    U -= 1
                else:
                    H -= visited[i][j] + 1 + U
                if H == 0:
                    continue


                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1



N, H, D = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(N)]

si, sj = -1, -1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'S':
            si = i
            sj = j
            break
    if si != -1:
        break

dis = bfs(si, sj, 0)
print(dis)
