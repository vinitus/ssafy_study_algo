def dfs(n):
    global ans
    vsted[n] = True
    ans += 1

    for i in graph[n]:
        if not vsted[i]:
            dfs(i)

N = int(input())    # 노드의 수
M = int(input())    # 간선의 수

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

vsted = [False] * (N + 1)
ans = 0
dfs(1)

print(ans - 1)