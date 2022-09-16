import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def check(y,x,N):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False

def findOne(arr):
    tmp = []
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] == 1:
                tmp.append((y,x))
    return tmp


N = int(input())
chess = list(list(map(int,input().split())) for _ in range(N))
dia1 = list(["*"] * (abs(i)) + [] for i in range(-N+1,N))
for j in range(N):
    for i in range(N):
        dia1[i+j] += [(chess[j][i]),"*"]
one = findOne(dia1)
print(one)
# * * * * 1 *
# * * * 1 * 0 *
# * * 0 * 1 * 1 *
# * 1 * 0 * 0 * 1 *
# 1 * 0 * 1 * 0 * 1 *
# * 0 * 0 * 0 * 0 *
# * * 1 * 0 * 1 *
# * * * 0 * 1 *
# * * * * 1 *

visited = {"x":[],"y":[]}

def bfs(visited, one, dia, cnt, one_visited):
    global answer
    if one_visited[-1] == 1:
        if cnt > answer:
            answer = cnt
        return
    # print(one)
    # for i in dia1:
    #     print(*i)
    for i in range(len(one)):
        y,x = one[i][0], one[i][1]
        if not one_visited[i] and y not in visited["y"] and x not in visited["x"]:
            one_visited[i] = 1
            visited["y"] += [y]
            visited["x"] += [x]
            dia[y][x] = "B"
            bfs(visited,one,dia,cnt+1,one_visited)
            one_visited[i] = 0
            visited["y"].pop()
            visited["x"].pop()
            dia[y][x] = 1

one_visited = list([0] * len(one))
answer = 0
bfs(visited,one,dia1,0,one_visited)
print(answer)