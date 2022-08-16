from heapq import heappush, heappop, heapify
import sys
input = sys.stdin.readline

N = int(input().strip())
lst = []
for _ in range(N):
    i = int(input().strip())
    if not lst and i == 0:
        print(0)
    elif i == 0:
        print(-heappop(lst))
    else:
        heappush(lst, -i)