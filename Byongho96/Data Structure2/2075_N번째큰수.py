## 메모리 제한 문제
## 우선순위 큐를 사용
## 2164ms...
import heapq
import sys
input = sys.stdin.readline

# N = int(input())
#
# heap = []
# for _ in range(N):
#     for num in map(int, input().rstrip().split()):
#         if len(heap) < N + 1:   # N+1개의 데이터를 유지
#             heapq.heappush(heap, num)  # 최댓값 연산
#         else:
#             heapq.heappop(heap) # 최솟값은 제외
#             heapq.heappush(heap, num)
#
# if N == 1:
#     print(heap[0])
# else:
#     heapq.heappop(heap)     # 1개는 out
#     print(heap[0])

################################################
# N+1개의 데이터에서 한개를 무조건 빼는게 아니라, N개의 데이터를 두고 비교해서 클때만 빼기
# 900ms

N = int(input())

heap = list(map(int, input().rstrip().split()))
heapq.heapify(heap)  # 첫번째 열

for _ in range(N-1):
    for num in map(int, input().rstrip().split()):
        if heap[0] < num:   # 데이터가 클 경우에만 넣기
            heapq.heappop(heap) # 최솟값은 제외
            heapq.heappush(heap, num)

print(heap[0])