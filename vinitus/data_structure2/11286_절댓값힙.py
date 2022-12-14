from heapq import heappop,heappush
import sys
input = sys.stdin.readline

N = int(input().strip())
lst = []
for _ in range(N):
    i = int(input())
    if not lst and i == 0:
        print(0)
    elif i == 0:
        print(heappop(lst)[1])
    else:
        heappush(lst,[abs(i),i])