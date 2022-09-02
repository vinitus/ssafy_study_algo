import sys
from heapq import heappush, heappop

input = sys.stdin.readline
T = int(input())
for i in range(T):
    pq_min = []
    pq_max = []
    cnt = {}
    k = int(input())
    for j in range(k):
        e, v = input().split()
        v = int(v)
        if e == 'I':
            try:
                if cnt[v] < 1:
                    heappush(pq_max, -v) if cnt[v] == 0 else heappush(pq_min, v)
                    cnt[v] = 1
                else:
                    cnt[v] += 1
            except:
                cnt[v] = 1
                heappush(pq_min, v)
                heappush(pq_max, -v)
        elif pq_min and pq_max:
            now = pq_min[0] if v < 0 else -pq_max[0]
            cnt[now] -= 1
            if cnt[now] == 0:
                if v < 0:
                    heappop(pq_min)
                    cnt[now] = -1
                else:
                    heappop(pq_max)
            while pq_min and cnt[pq_min[0]] < 1:
                cnt.pop(heappop(pq_min))
            while pq_max and cnt[-pq_max[0]] < 1:
                cnt.pop(-heappop(pq_max))
    if pq_min:
        print(-pq_max[0], pq_min[0])
    else:
        print('EMPTY')