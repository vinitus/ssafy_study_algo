# 68 ms
import sys
input = sys.stdin.readline

def dfs(v):
    visited = [0] * (N + 1)
    stk = []

    visited[v] = 1
    cnt = 0
    while True:
        for w in adjLst[v]:
            if not visited[w]:
                stk.append(v)
                v = w
                visited[v] = 1
                cnt += 1
                break
        else:
            if stk:
                v = stk.pop()
            else:
                break
    return cnt

N = int(input())
adjLst = [[] for _ in range(N+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    adjLst[a].append(b)
    adjLst[b].append(a)

print(dfs(1))