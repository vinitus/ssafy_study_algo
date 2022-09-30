from collections import deque


def dfs(V):
    global dfs_cnt
    vsted[V] = 1
    dfs_rlt[dfs_cnt] = V
    dfs_cnt += 1

    for j in range(N + 1):
        if adj_arr[V][j] == 1 and not vsted[j]:
            dfs(j)


def bfs(S):
    global bfs_cnt
    q = deque()
    q.append(S)
    vsted[S] = 1

    while q:
        v = q.popleft()
        bfs_rlt[bfs_cnt] = v
        bfs_cnt += 1
        
        for j in range(N + 1):
            if adj_arr[v][j] == 1 and not vsted[j]:
                q.append(j)
                vsted[j] = 1
    

N, M, V = map(int, input().split())
adj_arr = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj_arr[s][e] = 1
    adj_arr[e][s] = 1

dfs_rlt = [0] * N
vsted = [0] * (N + 1)
dfs_cnt = 0
dfs(V)

bfs_rlt = [0] * N
vsted = [0] * (N + 1)
bfs_cnt = 0
bfs(V)

for i in range(dfs_cnt):
    print(dfs_rlt[i], end=' ')
print()

for i in range(bfs_cnt):
    print(bfs_rlt[i], end=' ')
print()