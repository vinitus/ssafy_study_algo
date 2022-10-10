from collections import deque
import sys
input = sys.stdin.readline

# 424ms
def bfs(start):
    visited = [0] * (N + 1)
    q = deque()

    q.append(start)
    visited[start] = 1

    while q:
        # print('par', par)
        # print('q', q)
        v = q.popleft()
        for w in adjLst[v]:
            if not visited[w]:
                par[w] = v
                q.append(w)
                visited[w] = 1

N = int(input())
adjLst= [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adjLst[a].append(b)
    adjLst[b].append(a)

par = [0] * (N + 1)
bfs(1)

for p in par[2:]:
    print(p)

############################################################
# # 1640ms
# # dfs_stack
# def dfs(v):
#     visited = [0] * (N + 1)
#     stk = []
#
#     visited[v] = 1
#     while True:
#         # 종료조건 없음. 완전탐색
#         # 기본구조
#         for w in adjLst[v]:
#             if not visited[w]:
#                 stk.append(v)
#                 parent[w] = v   # 부모 노드 저장
#                 v = w
#                 visited[v] = 1
#                 break
#         else:
#             if stk:
#                 v = stk.pop()
#             else:
#                 break
#     return
#
# N = int(input())
# adjLst = [[] for _ in range(N+1)]
#
# for _ in range(N-1):
#     a, b = map(int, input().rstrip().split())
#     adjLst[a].append(b)
#     adjLst[b].append(a)
#
# parent = [0] * (N + 1)
# dfs(1)  # 1번 노드가 루트 노드
#
# for i in range(2, N + 1):
#     print(parent[i])