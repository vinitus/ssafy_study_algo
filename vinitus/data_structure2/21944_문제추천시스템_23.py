from heapq import heappush,heappop
import sys
def input():
    return sys.stdin.readline().rstrip()
# 필요한 자료 구조 선언
min_heap = []
max_heap = []
G_min = {}
G_max = {}
L_min = {}
L_max = {}
diffi_dct = {}

N = int(input())

for _ in range(N):
    P, L, G = map(int,input().split())
    heappush(max_heap, (-L,-P, -G))
    heappush(min_heap, (L,P, G))
    if G in G_max:
        heappush(G_max[G], (-L,-P))
        heappush(G_min[G], (L,P))
    else:
        G_max[G] = [(-L,-P)]
        G_min[G] = [(L,P)]
    if L in L_max:
        heappush(L_max[L], -P)
        heappush(L_min[L], P)
    else:
        L_max[L] = [-P]
        L_min[L] = [P]
    diffi_dct[P] = [L, G]

M = int(input())
for _ in range(M):
    lst = list(input().split())
    if lst[0] == "add":
        P,L,G = int(lst[1]),int(lst[2]),int(lst[3])
        heappush(max_heap, (-L, -P, -G))
        heappush(min_heap, (L, P, G))
        if G in G_max:
            heappush(G_max[G], (-L, -P))
            heappush(G_min[G], (L, P))
        else:
            G_max[G] = [(-L, -P)]
            G_min[G] = [(L, P)]
        if L in L_max:
            heappush(L_max[L], -P:)
            heappush(L_min[L], P)
        else
            L_max[L] = [-P]
            L_min[L] = [P]
        diffi_dct[P] = [L, G]

    elif lst[0] == "solved":
        P = int(lst[1])
        diffi_dct[P] = [0, 0]

    elif lst[0] == "recommend":
        G,x = int(lst[1]),int(lst[2])
        if x == -1:
            while diffi_dct[G_min[G][0][1]][1] == 0:
                heappop(G_min[G])
            while G != diffi_dct[G_min[G][0][1]][1]:
                heappop(G_min[G])
            print(G_min[G][0][1])
        else:
            while diffi_dct[-G_max[G][0][1]][1] == 0:
                heappop(G_max[G])
            while G != diffi_dct[-G_max[G][0][1]][1]:
                heappop(G_max[G])
            print(-G_max[G][0][1])
    elif lst[0] == "recommend2":
        x = int(lst[1])
        if x == -1:
            while min_heap[0][0] != diffi_dct[min_heap[0][1]][0]:
                heappop(min_heap)
            print(min_heap[0][1])
        else:
            while -max_heap[0][0] != diffi_dct[-max_heap[0][1]][0]:
                heappop(max_heap)
            print(-max_heap[0][1])
    elif lst[0] == "recommend3":
        x,L = int(lst[1]), int(lst[2])
        if x == 1:
            while L <= -max_heap[0][0]:
                if L in L_min and len(L_min[L]) != 0:
                    if L != diffi_dct[L_min[L][0]][0]:
                        heappop(L_min[L])
                        continue
                    print(L_min[L][0])
                    break
                L += 1
            else:
                print(-1)
        else:
            while L >= min_heap[0][0]:
                if L in L_max and len(L_max[L]) != 0:
                    if L != diffi_dct[-L_max[L][0]][0]:
                        heappop(L_max[L])
                        continue
                    print(-L_max[L][0])
                    break
                L -= 1
            else:
                print(-1)