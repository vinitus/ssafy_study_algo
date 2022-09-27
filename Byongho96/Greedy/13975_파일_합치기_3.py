# 최소 혹은 최대는 heap으로 구현
import heapq
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    chapters = []
    for num in input().rstrip().split():
        heapq.heappush(chapters, int(num))

    result = 0
    for _ in range(K-1):
        sm = heapq.heappop(chapters) + heapq.heappop(chapters)
        result += sm
        heapq.heappush(chapters, sm)

    print(result)
