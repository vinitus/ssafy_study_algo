import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    max_heap = []
    min_heap = []
    for _ in range(int(input())):
        S, N = input().rstrip().split()
        N = int(N)
        if S == 'I':
            heapq.heappush(max_heap, -N)
            heapq.heappush(min_heap, N)
        elif min_heap:
            if N == 1:
                mx = heapq.heappop(max_heap)
                min_heap.remove(-mx) # 어차피 리프에 있을 노드
            else:
                mn = heapq.heappop(min_heap)
                max_heap.remove(-mn) # 어차피 리프에 있을 노드

    if not min_heap:
        print('EMPTY')
        continue

    mx = -max_heap[0]
    mn = min_heap[0]
    print(f'{mx}, {mn}')