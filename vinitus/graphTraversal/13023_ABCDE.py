import sys
def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())
adj = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
    a, b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

def backtracking(idx, now):
    if now == 4:
        print(1)
        exit()
    for i in adj[idx]:
        if not visited[i]:
            visited[i] = True
            backtracking(i, now+1)
            visited[i] = False

for i in range(N):
    visited[i] = True
    backtracking(i, 0)
    visited[i] = False

print(0)