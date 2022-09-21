import sys


def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [[False] * N for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]

    mn = 1000000
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                c = 1
                ni = i
                nj = j
                while True:
                    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        nxi = ni + di
                        nxj = nj + dj
                        if 0 <= nxi < N and 0 <= nxj < N and arr[nxi][nxj] - arr[ni][nj] == 1:
                            c += 1
                            ni = nxi
                            nj = nxj
                            visited[nxi][nxj] = True
                            break
                    else:
                        break
                if c > cnt:
                    cnt = c
                    mn = arr[i][j]
                elif c == cnt:
                    mn = min(mn, arr[i][j])
    print(f'#{tc} {mn} {cnt}')


def dfs(row, col):
    num = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    r, c = row, col
    while True:
        visited[r][c] = True
        for i in range(4):
            tmp_x, tmp_y = r + dx[i], c + dy[i]
            if 0 <= tmp_x < N and 0 <= tmp_y < N and arr[r][c] + 1 == arr[tmp_x][tmp_y]:
                if visited[tmp_x][tmp_y]:
                    num += visited[tmp_x][tmp_y]
                    visited[row][col] = num
                    return num
                else:
                    num += 1
                    r, c = tmp_x, tmp_y
                    break
        else:
            visited[row][col] = num
            return num


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[None] * N for _ in range(N)]
    ans_val = 0
    ans_start = 0
    for row in range(N):
        for column in range(N):
            if not visited[row][column]:
                tmp_val = dfs(row, column)
                if tmp_val > ans_val:
                    ans_val, ans_start = tmp_val, arr[row][column]
                elif tmp_val == ans_val:
                    ans_start = min(ans_start, arr[row][column])
    print(f"#{test_case} {ans_start} {ans_val}")
