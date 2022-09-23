import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
arr = [[] for i in range(N + 1)]

for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)
ans = [None] * (N + 1)


def bfs():
    stack = [1]
    visited = [None] * (N + 1)

    while stack:
        cur = stack.pop()
        # 방문 조회

        if visited[cur]:
            continue

        visited[cur] = True
        for num in arr[cur]:

            if not visited[num]:
                ans[num] = cur
                stack.append(num)


bfs()
print(*ans[2:], sep='\n')
