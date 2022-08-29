import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def subset(stk):
    global N, min_value, road
    if len(stk) == N:
        sum_stk = stk.pop()
        if road[stk[-1]][stk[0]] == 0:
            return
        sum_stk += road[stk[-1]][stk[0]]
        if sum_stk < min_value:
            min_value = sum_stk
        return

    for i in range(N):
        if len(stk) > 1 and i in stk:
            continue
        if road[stk[-1]][i] == 0:
            continue
        sum_stk = stk.popleft()
        sum_stk += road[stk[-1]][i]
        stk.append(i)
        stk.appendleft(sum_stk)
        subset(stk)
        stk.pop()

N = int(input())
W = list(list(map(int,input().split())) for _ in range(N))
road = list({} for _ in range(N))

for y in range(N):
    for x in range(N):
        if y == x:
            continue
        road[y][x] = W[y][x]

min_value = 1000000*10

subset(deque([0]))

print(min_value)