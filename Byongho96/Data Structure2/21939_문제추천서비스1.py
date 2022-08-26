## 문제 잘 읽기
## add(P, L) 추천 문제 리스트에 없는 문제 번호 P만 입력으로 주어진다. 이전에 추천 문제 리스트에 있던 문제 번호가 다른 난이도로 다시 들어 올 수 있다.)
import heapq
import sys
input = sys.stdin.readline

# # 그냥 리스트 in 리스트 구현: 시간초과. PyPy3 516ms
# class ProblemReco():
#     def __init__(self):
#         self.L_lst = [[] for _ in range(101)]
#         self.P_lst = [0] * 100001
#     def recommended(self, X):
#         if X == '1':
#             for L in self.L_lst[::-1]:
#                 if L:
#                     L.sort()
#                     return L[-1]
#         else:
#             for L in self.L_lst:
#                 if L:
#                     L.sort()
#                     return L[0]
#
#     def add(self, P, L):
#         self.L_lst[L].append(P)
#         self.P_lst[P] = L
#
#     def solved(self, P):
#         self.L_lst[self.P_lst[P]].remove(P)
#
# service = ProblemReco()
#
# N = int(input())
# for _ in range(N):
#     P, L = map(int, input().rstrip().split())
#     service.add(P, L)
#
# M = int(input())
# for _ in range(M):
#     cmd = input().rstrip()
#     if cmd[0] == 'a':
#         cmd, P, L = cmd.split()
#         service.add(int(P), int(L))
#     elif cmd[0] == 's':
#         cmd, P = cmd.split()
#         service.solved(int(P))
#     else:
#         cmd, X = cmd.split()
#         print(service.recommended(X))

##########################################################
# 힙구현 328ms
class ProblemReco():
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.visited = [0] * 100001
    def recommend(self, X):
        if X == 1:
            while self.visited[-self.max_heap[0][1]] != -self.max_heap[0][0]:
                heapq.heappop(self.max_heap)
            print(-self.max_heap[0][1])
        else:
            while self.visited[self.min_heap[0][1]] != self.min_heap[0][0]:
                heapq.heappop(self.min_heap)
            print(self.min_heap[0][1])
    def add(self, P, L):
        heapq.heappush(self.min_heap, (L, P))
        heapq.heappush(self.max_heap, (-L, -P))
        self.visited[P] = L
    def solved(self, P):
        self.visited[P] = 0

service = ProblemReco()

N = int(input())
for _ in range(N):
    P, L = map(int, input().rstrip().split())
    service.add(int(P), int(L))

K = int(input())
for _ in range(K):
    string = input().rstrip()
    if string[0] == 'a':
        s, P, L = string.split()
        service.add(int(P), int(L))
    elif string[0] == 's':
        s, P = string.split()
        service.solved(int(P))
    else:
        s, X = string.split()
        service.recommend(int(X))

