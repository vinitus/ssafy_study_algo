from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def inorder_row(cur, level):
    global row
    global max_level
    if cur != -1:
        inorder_row(ch1[cur], level + 1)
        row += 1
        levels[level].append(row)
        max_level = max(max_level, level)
        inorder_row(ch2[cur], level + 1)

N = int(input())
par = [0] * (N+1)
ch1 = [0] * (N+1)
ch2 = [0] * (N+1)
for i in range(1, N+1):
    num, c1, c2 = map(int, input().split())
    ch1[num] = c1
    ch2[num] = c2
    # c1이 -1일 때 주의!!!!!!!!!!!!!
    if c1 != -1:
        par[c1] = num
    if c2 != -1:
        par[c2] = num

# root 찾기
root = 1
while par[root]:
    root = par[root]

# level별 row형성하기
row = 0
max_level = 0
levels = [[]for _ in range(10001)]
inorder_row(root, 1)

# 제일 넓은 너비와 레벨 찾기
level = 0
max_width = 0
for i in range(1, max_level + 1):
    width = levels[i][-1] - levels[i][0] + 1
    # print('i:', i, width)
    if width > max_width:
        max_width = width
        level = i

print(level, max_width)

