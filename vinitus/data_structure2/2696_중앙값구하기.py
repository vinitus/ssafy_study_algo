from heapq import heappush,heappop
import sys
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for t in range(T):
    N = int(input())
    
    lst = []
    min_heap = []
    max_heap = []
    min_cnt = 0
    max_cnt = 0
    for i in range(N//10+1):
        lst.extend(list(map(int,input().split())))
    middle = lst[0]
    print(N//2+1)
    print(middle, end = " ")
    for i in range(1,N):
        if lst[i] < middle:
            heappush(max_heap, -lst[i])
            max_cnt += 1
        else:
            heappush(min_heap, lst[i])
            min_cnt += 1

        if i % 2 == 0:
            if max_cnt > min_cnt:
                heappush(min_heap, middle)
                middle = -heappop(max_heap)
                max_cnt -= 1
                min_cnt += 1
            elif max_cnt < min_cnt:
                heappush(max_heap, -middle)
                middle = heappop(min_heap)
                max_cnt += 1
                min_cnt -= 1
            print(middle, end= " ")
    print()