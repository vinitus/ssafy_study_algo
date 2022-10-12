from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    visited = [0] * (N + 1)
    q = deque()
    visited[v] = 1
    q.append(v)
    while q:
        v = q.popleft()
        for w in adjLst[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                q.append(w)
    mx_idx = -1
    mx = 0
    for i in range(N + 1):
        if visited[i] > mx:
            mx = visited[i]
            mx_idx = i
    return mx_idx, mx - 1

N = int(input())
adjLst = [[] for _ in range(N + 1)]
# par = [0] * (N + 1)

circles = [[] for _ in range(N + 1)]
circles[N] = [0, 0, 2000001]            # 최댓값 설정 주의
for i in range(N):
    circles[i] = list(map(int, input().split()))
circles.sort(key=lambda x:x[2])

# print(circles)

for i in range(N):
    ci, cj, cr = circles[i]
    for j in range(i+1, N + 1):
        pi, pj, pr = circles[j]
        if abs(ci-pi) ** 2 + abs(cj-pj) ** 2 < pr ** 2:
            adjLst[i].append(j)
            adjLst[j].append(i)
            break
# print(adjLst)

one, _ = bfs(0)
another, result = bfs(one)

print(result)