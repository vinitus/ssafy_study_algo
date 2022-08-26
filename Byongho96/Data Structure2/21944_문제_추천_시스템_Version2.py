# 788ms
import heapq
import sys
input = sys.stdin.readline

class ProblemService:
    MX_heap = []
    MN_heap = []
    exist = [0] * 100001
    def __init__(self):
        self.mx_heap = []
        self.mn_heap = []

    def add(self, P, L, G):             # L뿐만 아니라 G까지 고려해줘야 한다!! 문제번호와 레벨이 같더라도, G가 다르면 다른 문제!!
        heapq.heappush(self.mx_heap, (-L, -P, G))
        heapq.heappush(self.mn_heap, (L, P, G))

    @classmethod
    def cls_add(cls, P, L, G):
        heapq.heappush(cls.MX_heap, (-L, -P, G))
        heapq.heappush(cls.MN_heap, (L, P, G))
        cls.exist[P] = (L, G)

    def recommend(self, X):
        if X == 1:
            while self.mx_heap and ProblemService.exist[-self.mx_heap[0][1]] != (-self.mx_heap[0][0], self.mx_heap[0][2]):
                heapq.heappop(self.mx_heap)
            if self.mx_heap:
                return self.mx_heap[0]
        else:
            while self.mn_heap and ProblemService.exist[self.mn_heap[0][1]] != (self.mn_heap[0][0], self.mn_heap[0][2]):
                heapq.heappop(self.mn_heap)
            if self.mn_heap:
                return self.mn_heap[0]

    @classmethod
    def cls_recommend(cls, X):
        if X == 1:
            while ProblemService.exist[-cls.MX_heap[0][1]] != (-cls.MX_heap[0][0], cls.MX_heap[0][2]):
                heapq.heappop(cls.MX_heap)
            return cls.MX_heap[0]
        else:
            while ProblemService.exist[cls.MN_heap[0][1]] != (cls.MN_heap[0][0], cls.MN_heap[0][2]):
                heapq.heappop(cls.MN_heap)
            return cls.MN_heap[0]

    @classmethod
    def solved(cls, P):
        cls.exist[P] = 0

group = [0] * 101
level = [0] * 101
for i in range(1, 101):
    group[i] = ProblemService()
    level[i] = ProblemService()

N = int(input())
for _ in range(N):
    P, L, G = map(int, input().rstrip().split())
    group[G].add(P, L, G)
    level[L].add(P, L, G)
    ProblemService.cls_add(P, L, G)

M = int(input())
for _ in range(M):
    string = input().rstrip()
    if string[0] == 'a':
        _, P, L, G = string.split()
        P = int(P)
        L = int(L)
        G = int(G)
        group[G].add(P, L, G)
        level[L].add(P, L, G)
        ProblemService.cls_add(P, L, G)
    elif string[0] == 's':
        _, P = string.split()
        P = int(P)
        ProblemService.solved(P)
    elif string[9] == ' ':
        _, G, X = string.split()
        G = int(G)
        X = int(X)
        reco = group[G].recommend(X)
        if X > 0:
            print(-reco[1])
        else:
            print(reco[1])
    elif string[9] == '2':
        _, X = string.split()
        X = int(X)
        reco = ProblemService.cls_recommend(X)
        if X > 0:
            print(-reco[1])
        else:
            print(reco[1])
    else:
        _, X, L = string.split()
        X = int(X)
        L = int(L)
        if X > 0:
            for i in range(L, 101):
                reco = level[i].recommend(-X)
                if reco:
                    print(reco[1])
                    break
            else:
                print(-1)
        else:
            for i in range(L-1, 0, -1):
                reco = level[i].recommend(-X)
                if reco:
                    print(-reco[1])
                    break
            else:
                print(-1)