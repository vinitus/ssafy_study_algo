import sys
input = sys.stdin.readline
# 1276ms / 30840KB
def dfs(n, cur):
    global result
    if n == 4:
        result = 1
        return
    if result == 1:
        return
    for next in adjLst[cur]:
        if not visited[next]:
            visited[next] = 1
            dfs(n+1, next)
            visited[next] = 0

N, M = map(int, input().split())
adjLst = [[]for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    adjLst[a].append(b)
    adjLst[b].append(a)

result = 0
for i in range(N):
    visited = [0] * N
    visited[i] = 1
    dfs(0, i)
    if result:
        print(result)
        break
else:
    print(result)


####################################
# 1592ms / 30840KB
N, M = map(int, input().split())
adjLst = [[]for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    adjLst[a].append(b)
    adjLst[b].append(a)

result = 0
for i in range(N):

    for j in adjLst[i]:
        if j != i:

            for k in adjLst[j]:
                if k not in (i, j):

                    for l in adjLst[k]:
                        if l not in (i, j, k):

                            for m in adjLst[l]:
                                if m not in (i, j, k, l):
                                    result = 1
                                    break

                            if result:
                                break

                    if result:
                        break

            if result:
                break

    if result:
        break

print(result)
