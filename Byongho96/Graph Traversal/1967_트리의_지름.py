from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

# 112ms
def farthest_node(v):
    visited = [-1] * (N + 1)
    q = deque()

    visited[v[0]] = v[1]
    q.append(v)
    while q:
        v = q.popleft()
        for w in adjLst[v[0]]:
            if visited[w[0]] == -1:
                q.append(w)
                visited[w[0]] = visited[v[0]] + w[1]
    distance = max(visited)
    return visited.index(distance), distance


N = int(input())
adjLst = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, w = map(int, input().split())
    adjLst[a].append((b, w))
    adjLst[b].append((a, w))

leaf1, _ = farthest_node((1, 0))
leaf2, radius = farthest_node((leaf1, 0))

print(radius)

#######################################################\
# # 시간초과22222
# def find_ancestors(cur):
#     ancestors = [cur]
#     distance = [0]
#     while cur != 1:
#         parent = par[cur]
#         ancestors.append(parent[0])
#         distance.append(parent[1] + distance[-1])
#         cur = parent[0]
#     return ancestors, distance
#
# N = int(input())
# par = [0] * (N + 1)
# for _ in range(N - 1):
#     p, c, w = map(int, input().split())
#     par[c] = (p, w)
#
# # find leaves
# leaves = []
# for i in range(1, N + 1):
#     if i not in par:
#         leaves.append(i)
#
# mx = 0
# for comb in combinations(leaves, 2):
#     an1, d1 = find_ancestors(comb[0])
#     an2, d2 = find_ancestors(comb[1])
#     if d1[-1] + d2[-1] < mx:
#         continue
#     diameter = 0
#     for i, an in enumerate(an1):
#         if an in an2:
#             diameter = d1[i] + d2[an2.index(an)]
#             break
#     mx = max(mx, diameter)
#
# print(mx)

#######################################################
# # 시간초과
# def dfs(v):
#     visited = [-1] * (N + 1)
#     stk = []
#
#     visited[v[0]] = 0
#
#     while True:
#         # visit(v)
#         if -1 in visited[v[0]:]:
#             pass
#         else:
#             return max(visited)
#         for w in adjLst[v[0]]:
#             if visited[w[0]] == -1:
#                 stk.append(v)
#                 visited[w[0]] = visited[v[0]] + w[1]
#                 v = w
#                 break
#         else:
#             if stk:
#                 v = stk.pop()
#             else:
#                 break
#
# N = int(input())
# adjLst = [[] for _ in range(N + 1)]
# for _ in range(N - 1):
#     a, b, w = map(int, input().split())
#     adjLst[a].append((b, w))
#     adjLst[b].append((a, w))
#
# mx = 0
# for start in range(1, N + 1):
#     mx = max(mx, dfs((start, 0)))
#
# print(mx)