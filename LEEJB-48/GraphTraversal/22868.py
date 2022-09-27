import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10 ** 4)

#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")


#############################

def first_dfs(s):
    stack = deque([[s]])
    visited[s] = True
    while stack:
        tmp = deque()
        for _ in range(len(stack)):
            cur = stack.popleft()
            last = cur[-1]
            if last == end:
                return cur
            for num in graph[last]:
                if not visited[num]:
                    visited[num] = True
                    tmp.append(cur + [num])
        stack = tmp
    return None


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N + 1):
    graph[i].sort()
start, end = map(int, input().split())

visited = [False] * (N + 1)
S = first_dfs(start)

visited = [False] * (N + 1)
for i in S:
    visited[i] = True
start, end = end, start
visited[start], visited[end] = False, False

E = first_dfs(start)

print(len(S) + len(E) - 2)
