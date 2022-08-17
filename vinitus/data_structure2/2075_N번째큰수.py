from heapq import heappop,heappush
from queue import PriorityQueue


N = int(input())
que = PriorityQueue(maxsize=N)
que.put()
tmp = list(map(int,input().split()))
heapify(tmp)
for _ in range(N-1):
    heapify(tmp) 