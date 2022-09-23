import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")

#############################
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(r, c, num):
    if len(num) == 7:
        num_set.add(num)
        return None
    if num in dp[len(num)][r][c]:
        return None
    dp[len(num)][r][c].add(num)
    for k in range(4):
        mx = r + dx[k]
        my = c + dy[k]
        if 0 <= mx < 4 and 0 <= my < 4:
            bfs(mx, my, num + arr[mx][my])


T = int(input())

for test_case in range(1, T + 1):
    num_set = set()
    arr = [input().split() for _ in range(4)]
    dp = [[[set() for _ in range(4)] for __ in range(4)] for _ in range(8)]
    for i in range(4):
        for j in range(4):
            bfs(i, j, "")
    print(f"#{test_case} {len(num_set)}")
