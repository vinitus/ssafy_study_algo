# 발표 준비
# 작은 수 끼리 먼저 합쳐야 최솟값이 될 수 있다.
# 최솟값 2개를 빼서 더해주고 다시 자료구조에 넣어준다.
    # 이를 구현하기 위해 매번 sort를 반복하는 것 보다, 최소힙을 만드는 것이 낫다.
    # 최소힙
        # 자식 노드가 부모 노드보다 큰 완전 이진 트리. 
        # 루트 노드가 트리의 최솟값이 된다.
    # heappop 연산 : 최소힙의 루트를 출력
from heapq import heappush, heappop
import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    data = list(map(int, input().split()))

    min_heap = []
    for ele in data:
        heappush(min_heap, ele)

    ans = 0
    while len(min_heap) > 1:
        temp = heappop(min_heap) + heappop(min_heap)
        ans += temp
        heappush(min_heap, temp)

    print(ans)