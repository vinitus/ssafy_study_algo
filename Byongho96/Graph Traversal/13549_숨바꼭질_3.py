# 132 ms
from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    visited = [0] * 100001
    q = deque()

    visited[v] = 1
    q.append(v)
    while q:
        v = q.popleft()
        # print(v, q, visited[v])
        for w, time in ((2*v,0), (v-1,1), (v+1,1)):
            if 0<=w<=K+1 and not visited[w]:        # 범위를 K + 1까지
                visited[w] = visited[v] + time
                if w == K:
                    return visited[w] - 1
                if not time:
                    q.appendleft(w)
                else:
                    q.append(w)

N, K = map(int, input().split())
if K <= N:
    print(N - K)
else:
    mn_time = K - N
    print(bfs(N))

