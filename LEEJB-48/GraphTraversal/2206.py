import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")


#############################
def bfs():
    global ans
    queue = deque()
    queue.append((0, 0))
    visited = [[False] * C for _ in range(R)]
    cnt = 1
    while queue:
        if cnt >= ans:
            return None
        for _ in range(len(queue)):
            cur = queue.popleft()

            if cur[0] + 1 == R and cur[1] + 1 == C:
                ans = cnt
                return None
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                tmp_x = x + cur[0]
                tmp_y = y + cur[1]
                if 0 <= tmp_x < R and 0 <= tmp_y < C and not matrix[tmp_x][tmp_y] and not visited[tmp_x][tmp_y]:
                    visited[tmp_x][tmp_y] = True
                    queue.append((tmp_x, tmp_y))
        cnt += 1


def find_candidate():
    queue = deque()
    queue.append((0, 0))
    candidates = []
    visited = [[False] * C for _ in range(R)]
    while queue:
        cur = queue.popleft()
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tmp_x = x + cur[0]
            tmp_y = y + cur[1]
            if 0 <= tmp_x < R and 0 <= tmp_y < C:
                if not visited[tmp_x][tmp_y]:
                    if matrix[tmp_x][tmp_y]:
                        candidates.append((tmp_x, tmp_y))
                    else:
                        queue.append((tmp_x, tmp_y))
                    visited[tmp_x][tmp_y] = True
    return candidates


def find_candidate_from_end():
    queue = deque()
    queue.append((R - 1, C - 1))
    candidates2 = []
    visited = [[False] * C for _ in range(R)]
    while queue:
        cur = queue.popleft()
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tmp_x = x + cur[0]
            tmp_y = y + cur[1]
            if 0 <= tmp_x < R and 0 <= tmp_y < C:
                if not visited[tmp_x][tmp_y]:
                    if matrix[tmp_x][tmp_y]:
                        candidates2.append((tmp_x, tmp_y))
                    else:
                        queue.append((tmp_x, tmp_y))
                    visited[tmp_x][tmp_y] = True
    return candidates2


R, C = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(R)]
candidate = find_candidate()
ans = float('inf')

bfs()
if ans == R + C - 1:
    print(ans)
else:
    if ans == float('inf'):
        another_candidate = find_candidate_from_end()
        x = set(another_candidate).intersection(set(candidate))
        if x:
            for r, c in list(x):
                if ans == R + C - 1:
                    break
                matrix[r][c] = 0
                bfs()
                matrix[r][c] = 1
            print(ans)
        else:
            print(-1)
    else:
        for r, c in candidate:
            if ans == R + C - 1:
                break
            matrix[r][c] = 0
            bfs()
            matrix[r][c] = 1
        print(ans)
