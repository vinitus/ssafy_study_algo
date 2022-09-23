import sys


def input():
    return sys.stdin.readline().rstrip()


R, C = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(cnt):
    visited = [[False] * C for _ in range(R)]
    stack = [(cnt, cnt)]
    to_be_deleted = []
    r = R - cnt
    c = C - cnt

    while stack:
        cur = stack.pop()
        if visited[cur[0]][cur[1]]:
            continue
        visited[cur[0]][cur[1]] = True
        for i in range(4):
            tmp_x = cur[0] + dx[i]
            tmp_y = cur[1] + dy[i]
            if cnt <= tmp_x < r and cnt <= tmp_y < c:
                if visited[tmp_x][tmp_y]:
                    continue
                if arr[tmp_x][tmp_y]:
                    to_be_deleted.append((tmp_x, tmp_y))
                    visited[tmp_x][tmp_y] = True
                else:
                    stack.append((tmp_x, tmp_y))
    if to_be_deleted:
        for r, c in to_be_deleted:
            arr[r][c] = 0
        return len(to_be_deleted)

    else:
        return 0


arr = [list(map(int, input().split())) for _ in range(R)]
cheese = sum([arr[i].count(1) for i in range(R)])
cnt = 0
while True:
    # bfs는 없어진 치즈개수를 반환한다
    sub = bfs(cnt)
    if sub > 0:
        prev_cheese = cheese
        cheese -= sub

        cnt += 1
    else:
        break

print(cnt)
print(prev_cheese)
