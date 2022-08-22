import sys
import heapq
input = sys.stdin.readline

## 밑에처럼 풀면 안됨!!!! 삭제할 때마다 삭제하는 값을 업데이트 해야함
# for _ in range(int(input())):
#     max_heap = []
#     min_heap = []
#     insert_num = 0
#     for _ in range(int(input())):
#         S, N = input().rstrip().split()
#         N = int(N)
#         if S == 'I':
#             heapq.heappush(max_heap, -N)
#             heapq.heappush(min_heap, N)
#             insert_num += 1
#         elif insert_num:
#             if N == 1:
#                 mx = heapq.heappop(max_heap)
#             else:
#                 mn = heapq.heappop(min_heap)
#             insert_num -= 1
#     print(max_heap, min_heap)
#     if insert_num:
#         while -max_heap[0] not in min_heap:
#             heapq.heappop(max_heap)
#         while -min_heap[0] not in max_heap:
#             heapq.heappop(min_heap)
#         mx = -max_heap[0]
#         mn = min_heap[0]
#         print(mx, mn)
#
#     else:
#         print('EMPTY')

## 삭제여부를 표시하는 리스트 배열,...
## 7380ms
for _ in range(int(input())):
    K = int(input())
    max_heap = []
    min_heap = []
    exist = [1] * K
    for i in range(K):
        S, N = input().rstrip().split()
        N = int(N)
        if S == 'I':
            heapq.heappush(max_heap, (-N, i))
            heapq.heappush(min_heap, (N, i))
        elif N == 1:
            while max_heap and not exist[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                exist[heapq.heappop(max_heap)[1]] = 0
        else:
            while min_heap and not exist[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                exist[heapq.heappop(min_heap)[1]] = 0
    # print(max_heap, min_heap)
    while max_heap and not exist[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not exist[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')


