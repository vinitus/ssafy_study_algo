from heapq import heappush,heappop
import sys
def input():
    return sys.stdin.readline().rstrip()
heap = []
heap2 = []
N = int(input())
dct = {}
for _ in range(N):
    P, L = map(int,input().split())
    heappush(heap,(L,P))
    heappush(heap2,(-L,-P))
    dct[P] = L
M = int(input())
for _ in range(M):
    lst = list(input().split())
    if lst[0] == "add":
        if int(lst[1]) in dct:
            heappush(heap, (int(lst[2]), int(lst[1])))
            heappush(heap2, (-int(lst[2]), -int(lst[1])))
            dct[int(lst[1])] = int(lst[2])
        else:
            heappush(heap, (int(lst[2]), int(lst[1])))
            heappush(heap2, (-int(lst[2]), -int(lst[1])))
            dct[int(lst[1])] = int(lst[2])
    elif lst[0] == "recommend":
        if lst[1] == "-1":
            while dct[heap[0][1]] == 0:
                heappop(heap)
            while dct[heap[0][1]] != heap[0][0]:
                heappop(heap)
            print(heap[0][1])
        else:
            while dct[-heap2[0][1]] == 0:
                heappop(heap2)
            while dct[-heap2[0][1]] != -heap2[0][0]:
                heappop(heap2)
            print(-heap2[0][1])

    else:
        dct[int(lst[1])] = 0