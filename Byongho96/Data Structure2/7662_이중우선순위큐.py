import sys
import heapq
input = sys.stdin.readline

################################################################################################

# # nlargest 사용: 시간초과
# for _ in range(int(input())):
#     K = int(input())
#     heap = []
#
#     for _ in range(K):
#         s, N = input().rstrip().split()
#         N = int(N)
#         if s == 'I':
#             heapq.heappush(heap, N)
#         elif heap:
#             if N < 0:
#                 heapq.heappop(heap)
#             else:
#                 heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
#
#     if heap:
#         print(heapq.nlargest(1, heap)[0], heap[0])
#     else:
#         print('EMPTY')


################################################################################################

# ## 삭제여부를 표시하는 리스트 배열,...
# ## 7380ms
# for _ in range(int(input())):
#     K = int(input())
#     max_heap = []
#     min_heap = []
#     exist = [1] * K                                   # i번째 입력한 숫자가 존재하는 지 여부를 체크하는 리스트
#     for i in range(K):
#         S, N = input().rstrip().split()
#         N = int(N)
#         if S == 'I':
#             heapq.heappush(max_heap, (-N, i))             # index와 함께 튜플로 만들어서 push
#             heapq.heappush(min_heap, (N, i))
#         elif N == 1:
#             while max_heap and not exist[max_heap[0][1]]: # exist array를 확인하면서, 실제 존재하는 최댓값이 나올때까지 pop
#                 heapq.heappop(max_heap)
#             if max_heap:                                  # 실제 최댓값을 팝하면, exist array 업데이트
#                 exist[heapq.heappop(max_heap)[1]] = 0
#         else:
#             while min_heap and not exist[min_heap[0][1]]: # exist array를 확인하면서, 실제 존재하는 최솟값이 나올때까지 pop
#                 heapq.heappop(min_heap)
#             if min_heap:                                  # 실제 최솟값을 팝하면, exist array 업데이트
#                 exist[heapq.heappop(min_heap)[1]] = 0

#     # print(max_heap, min_heap)                       # 마지막 한번 더 동기화, 마지막 연산이 끝나고 나서 둘 중하나의 힙을 업데이트 해야 함
#     while max_heap and not exist[max_heap[0][1]]:
#         heapq.heappop(max_heap)
#     while min_heap and not exist[min_heap[0][1]]:
#         heapq.heappop(min_heap)
#
#     if min_heap and max_heap:                         # 적절한 값 print
#         print(-max_heap[0][0], min_heap[0][0])
#     else:
#         print('EMPTY')


