import sys


def input():
    return sys.stdin.readline().rstrip()


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def explode(r, c):
    arr[r][c] = 0
    for i in range(4):
        tmp_x = r + dx[i]
        tmp_y = c + dy[i]
        if 0 <= tmp_x < R and 0 <= tmp_y < C:
            arr[tmp_x][tmp_y] = 0
    return None


def bomberman(n):
    while n:
        # 3
        for row in range(R):
            arr[row] = [x + 2 for x in arr[row]]
        n -= 1
        if not n:
            break
        # 4
        explode_stack = []
        """for row in range(R):
            arr[row] = [x + 1 for x in arr[row]]"""
        for row in range(R):
            for column in range(C):
                if arr[row][column] >= 3:
                    explode_stack.append((row, column))
        for r, c in explode_stack:
            explode(r, c)
        n -= 1
    return None


R, C, N = map(int, input().split())
start = [input() for _ in range(R)]

if N == 1:
    print(*start, sep='\n')
else:

    if N % 2 == 0:
        print(*['O' * C] * R, sep='\n')
    else:
        arr = [[0] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if start[i][j] == 'O':
                    arr[i][j] = 1
        if N % 4 == 1:
            N = 4
        else:
            N = 2
        bomberman(N)
        ans = [''.join(['O' if arr[i][j] else '.' for j in range(C)]) for i in range(R)]
        print(*ans, sep='\n')
