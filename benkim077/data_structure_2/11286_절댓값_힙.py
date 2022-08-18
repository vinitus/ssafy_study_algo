import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())

h = []
for _ in range(N):
    cmd = int(input())

    if cmd != 0:
        heappush(h, (abs(cmd), cmd))
    else:
        if h:
            print(heappop(h)[1])
        else:
            print(0)