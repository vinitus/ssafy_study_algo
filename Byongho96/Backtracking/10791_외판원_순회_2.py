import sys
input = sys.stdin.readline

def dfs_recursive(n, cur, cost):
    global mn
    # 종료조건
    if n == N - 1:
        if arr[cur][start]:         # 마지막 돌아가는 길도 있나 확인!
            cost += arr[cur][start]
            if cost < mn:
                mn = cost
        return
    # 가지치기
    elif cost > mn:
        return
    # 후보군 출력
    else:
        for i in range(N):
            if (not visited[i]) and arr[cur][i] and i != start:
                visited[i] = 1
                # cost += arr[cur][i] << 이렇게 넣으면 따로 초기화를 해줘야 함!!
                dfs_recursive(n + 1, i, cost + arr[cur][i])
                visited[i] = 0
        return


N = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

mn = 1000000 * N
visited = [0] * N
for start in range(N):
    dfs_recursive(0, start, 0)

print(mn)
