import sys


def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")

#############################
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(jihoon, fire):
    cnt = 1
    jihoon_stack = [jihoon]
    fire_stack = fire
    while jihoon_stack:
        tmp_fire = []
        tmp_jihoon = []

        for _ in range(len(fire_stack)):
            cur = fire_stack.pop()

            visited[cur[0]][cur[1]] = True
            for k in range(4):
                tmp_x = cur[0] + dx[k]
                tmp_y = cur[1] + dy[k]
                if 0 <= tmp_x < R and 0 <= tmp_y < C and not visited[tmp_x][tmp_y]:
                    visited[tmp_x][tmp_y] = True
                    tmp_fire.append((tmp_x, tmp_y))
        for _ in range(len(jihoon_stack)):
            cur = jihoon_stack.pop()
            for k in range(4):
                visited[cur[0]][cur[1]] = True
                tmp_x = cur[0] + dx[k]
                tmp_y = cur[1] + dy[k]
                if 0 <= tmp_x < R and 0 <= tmp_y < C:
                    if visited[tmp_x][tmp_y]:
                        continue
                    else:
                        visited[tmp_x][tmp_y] = True
                        tmp_jihoon.append((tmp_x, tmp_y))
                else:
                    return cnt
        fire_stack = tmp_fire[:]
        jihoon_stack = tmp_jihoon[:]
        cnt += 1
    return None


R, C = map(int, input().split())

maze = [list(input()) for _ in range(R)]
impossible = True
visited = [[None] * C for _ in range(R)]
fire = []
for i in range(R):
    for j in range(C):
        if maze[i][j] == '#':
            visited[i][j] = True
        elif maze[i][j] == 'J':
            jihoon = (i, j)
        elif maze[i][j] == 'F':
            fire.append((i, j))
ans = dfs(jihoon, fire[:])
if not ans:
    ans = "IMPOSSIBLE"
print(ans)
