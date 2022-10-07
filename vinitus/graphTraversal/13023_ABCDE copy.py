#13023, ABCDE, 골드5
import sys


def dfs(now, cnt, already_go):
    # print(route, cur)
    global result, visited

    root = already_go[0]
    if len(visited[root]) < cnt:
        visited[root] = already_go

    if result == 1 or cnt >= 5:
        result = 1
        return
    elif now != -1:
        for f in friends[now]:
            if visited[f] and now not in visited[f] and root not in visited[f]:
                dfs(-1, cnt+len(visited[f]), already_go+visited[f])
            elif f not in already_go:
                dfs(f, cnt+1, already_go + [f])


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    friends = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        friends[a].append(b)
        friends[b].append(a)

    # 0번 사람의 친구부터 탐색해 나간다. 깊이가 5이상이면 result = 1
    result = 0
    visited = [[] for _ in range(N)]
    for i in range(N):
        visited[i] = [i]
        dfs(i, 1, [i])

    # print(visited)
    print(result)