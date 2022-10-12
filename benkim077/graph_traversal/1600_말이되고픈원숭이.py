from collections import deque
import sys
input = sys.stdin.readline
sys.stdin = open('input.txt')


h_di = [-1, -2, -2, -1, 1, 2, 2, 1]
h_dj = [-2, -1, 1, 2, 2, 1, -1, -2]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0, K, 0))

    while q:
        ci, cj, ck, c_cnt = q.popleft() # 현재 i, j, k, cnt값

        # 말처럼 갈 수 있는 경우
        if ck > 0:
            for i in range(8):
                ni, nj = ci + h_di[i], cj + h_dj[i]
                if 0 <= ni < H and 0 <= nj < W and data_map[ni][nj] != 1:
                    if vsted[ni][nj] == -1 or vsted[ni][nj] < ck - 1:
                        if ni == H - 1 and nj == W - 1:
                            return c_cnt + 1
                        vsted[ni][nj] = ck - 1
                        q.append((ni, nj, ck - 1, c_cnt + 1))
        
        # 말처럼 갈 수 없는 경우
        else:
            for i in range(4):
                ni, nj = ci + di[i], cj + dj[i]
                if 0 <= ni < H and 0 <= nj < W and data_map[ni][nj] != 1:
                    if vsted[ni][nj] == -1 or vsted[ni][nj] < ck:
                        if ni == H - 1 and nj == W - 1:
                            return c_cnt + 1
                        vsted[ni][nj] = ck
                        q.append((ni, nj, ck, c_cnt + 1))

    return -1


K = int(input())
W, H = map(int, input().split())
data_map = [list(map(int, input().split())) for _ in range(H)]
vsted = [[-1] * W for _ in range(H)]

print(bfs())