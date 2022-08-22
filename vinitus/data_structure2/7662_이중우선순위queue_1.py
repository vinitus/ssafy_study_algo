import heapq
import sys
T = int(sys.stdin.readline())


def program():
    K = int(sys.stdin.readline())
    minHeap, maxHeap = [],  []
    minPop, maxPop = [],  []

    for _ in range(K):
        cmd = sys.stdin.readline().split()
        # 삽입
        if cmd[0] == 'I':
            heapq.heappush(minHeap, int(cmd[1]))
            heapq.heappush(maxHeap, -int(cmd[1]))
        # 삭제
        elif cmd[0] == 'D':
            # 최댓값 삭제
            if cmd[1] == '1':
                # 비어있으면 무시
                if not maxHeap:
                    continue
                # 이미 minHeap 에서 삭제된 값들은 건너뜀
                while (maxHeap and minPop) and (-maxHeap[0] == -minPop[0]):
                    heapq.heappop(maxHeap)
                    heapq.heappop(minPop)
                # 건너뛰어 보니 비어있으면 무시
                if not maxHeap:
                    continue
                x = heapq.heappop(maxHeap)
                heapq.heappush(maxPop, -x)
            # 최솟값 삭제
            elif cmd[1] == '-1':
                # 비어있으면 무시
                if not minHeap:
                    continue
                # 이미 maxHeap 에서 삭제된 값들은 건너뜀
                while (minHeap and maxPop) and (minHeap[0] == maxPop[0]):
                    heapq.heappop(minHeap)
                    heapq.heappop(maxPop)
                # 건너뛰어 보니 비어있으면 무시
                if not minHeap:
                    continue
                x = heapq.heappop(minHeap)
                heapq.heappush(minPop, -x)

    # 마무리 하고 이중 힙에 남아있는 최대 최솟값 출력
    maxV, minV = 0, 0
    while (maxHeap and minPop) and (maxHeap[0] == minPop[0]):
        heapq.heappop(maxHeap)
        heapq.heappop(minPop)
    if not maxHeap:
        print("EMPTY")
        return
    maxV = -maxHeap[0]
    while (minHeap and maxPop) and (minHeap[0] == maxPop[0]):
        heapq.heappop(minHeap)
        heapq.heappop(maxPop)
    minV = minHeap[0]
    print(maxV, minV)
    return


for _ in range(T):
    program()
