import heapq
import sys
input = sys.stdin.readline

class ProblemReco2:
    MX_heap = []
    MN_heap = []
    exist = [0] * 100001
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
    def recommend(self, X):
        if X == 1:
            while self.max_heap and ProblemReco2.exist[-self.max_heap[0][1]] != -self.max_heap[0][0]:
                heapq.heappop(self.max_heap)
            if self.max_heap:
                return -self.max_heap[0][1]
            return
        else:
            while self.min_heap and ProblemReco2.exist[self.min_heap[0][1]] != self.min_heap[0][0]:
                heapq.heappop(self.min_heap)
            if self.min_heap:
                return self.min_heap[0][1]
            return
    # def recommend3(self, X, L):
    #     pass
    def add(self, P, L):
        heapq.heappush(self.min_heap, (L, P))
        heapq.heappush(self.max_heap, (-L, -P))
        ProblemReco2.cls_add(P, L)
    @classmethod
    def cls_add(cls, P, L):
        heapq.heappush(ProblemReco2.MN_heap, (L, P))
        heapq.heappush(ProblemReco2.MX_heap, (-L, -P))
        ProblemReco2.exist[P] = L
    @classmethod
    def solved(cls, P):
        cls.exist[P] = 0
    @classmethod
    def recommend2(cls, X):
        if X == 1:
            while ProblemReco2.exist[-cls.MX_heap[0][1]] != -cls.MX_heap[0][0]:
                heapq.heappop(cls.MX_heap)
            print(-cls.MX_heap[0][1])
        else:
            while ProblemReco2.exist[cls.MN_heap[0][1]] != cls.MN_heap[0][0]:
                heapq.heappop(cls.MN_heap)
            print(cls.MN_heap[0][1])
    @classmethod
    def recommend3(cls, X, L):
        if X == 1:
            tmp_MN = cls.MN_heap.copy()
            while tmp_MN and (ProblemReco2.exist[tmp_MN[0][1]] != tmp_MN[0][0] or tmp_MN[0][0] < L):
                heapq.heappop(tmp_MN)
            if tmp_MN:
                print(tmp_MN[0][1])
                return
            print(-1)
        else:
            tmp_MX = cls.MX_heap.copy()
            while tmp_MX and (ProblemReco2.exist[-tmp_MX[0][1]] != -tmp_MX[0][0] or -tmp_MX[0][0] > L):
                heapq.heappop(tmp_MX)
            if tmp_MX:
                print(-tmp_MX[0][1])
                return
            print(-1)

service = [0] * 101
level = [0] * 101
for i in range(1, 101):
    service[i] = ProblemReco2()
    level[i] = ProblemReco2()

N = int(input())
for _ in range(N):
    P, L, G = map(int, input().rstrip().split())
    service[G].add(P, L)
    level[int(L)].add(int(P), int(L))

K = int(input())
for _ in range(K):
    string = input().rstrip()
    if string[0] == 'a':
        string, P, L, G = string.split()
        service[int(G)].add(int(P), int(L))
        level[int(L)].add(int(P), int(L))
    elif string[0] == 's':
        string, P = string.split()
        ProblemReco2.solved(int(P))
    elif string[9] == ' ':
        string, G, X = string.split()
        print(service[int(G)].recommend(int(X)))
    elif string[9] == '2':
        string, X = string.split()
        ProblemReco2.recommend2(int(X))
    else:
        string, X, L = string.split()
        L = int(L)
        if X == '1':
            for i in range(L, 101):
                rlt = level[i].recommend(-1)
                if rlt:
                    print(rlt)
                    break
            else:
                print(-1)
        else:
            for i in range(L-1, 0, -1):
                rlt = level[i].recommend(1)
                if rlt:
                    print(rlt)
                    break
            else:
                print(-1)