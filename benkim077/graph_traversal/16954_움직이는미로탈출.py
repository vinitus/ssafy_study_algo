# 8방향으로 너비 우선 탐색
# 벽이 내려오는 것을 고려해야 하므로, 
    # q.popleft()한 위치가 벽이라면, continue 하는 방식으로 구현한다.
import sys
from collections import deque
sys.stdin = open('input.txt')

def move_wall():
    k = 0
    while k < len(wall_lst):
        wall_lst[k][0] += 1
        
        if wall_lst[k][0] > 7:
            data[wall_lst[k][0] - 1][wall_lst[k][1]] = '.'
            wall_lst.pop(k)
            continue
        
        data[wall_lst[k][0] - 1][wall_lst[k][1]] = '.'
        data[wall_lst[k][0]][wall_lst[k][1]] = '#'
        # vsted[[wall_lst[k][0]][wall_lst[k][1]]] = 0

        k += 1


def bfs():
    q = deque()
    q.append((si, sj))
    vsted[si][sj] = 1

    prev = 1
    while q:
        i, j = q.popleft()

        if vsted[i][j] != prev: # 길이가 바뀔 때, 
            move_wall()             # 벽을 옮기자
        prev = vsted[i][j]
        # print(vsted)

        if data[i][j] == '#':   # 도중에 #로 바뀐 경우
            continue                # 아무것도 안하고 그냥 넘김

        for di, dj in [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
            ni, nj = i + di, j + dj
            # if (ni, nj) == (i, j) and data[ni][nj] != '#':
            #     vsted[ni][nj] = vsted[i][j] + 1
            #     q.append((ni, nj))
            
            if 0 <= ni < 8 and 0 <= nj < 8 and not vsted[ni][nj] and data[ni][nj] != '#':
                vsted[ni][nj] = vsted[i][j] + 1
                q.append((ni, nj))


data = [list(input()) for _ in range(8)]

# 벽 찾기
wall_lst = []
for i in range(8):
    for j in range(8):
        if data[i][j] == '#':
            wall_lst.append([i, j])

# bfs
si, sj = 7, 0
vsted = [[0] * 8 for _ in range(8)]
bfs()

# 결과 출력
# print(vsted)
# print(data)
if vsted[0][7] == 0:
    print(0)
else:
    print(1)