import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())

h = []
for _ in range(N):
    cmd = int(input())

    if cmd == 0:
        if h:
            print(heappop(h))
        else:
            print(0)
    else:
        heappush(h, cmd)
