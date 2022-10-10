import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    N = int(input())
    preference = [0] + list(map(int, input().split()))
    visited = [0] * (N + 1)
    group = [0] * (N + 1)

    left = 0
    group_num = 0
    for idx in range(1, N + 1):
        if not visited[idx]:
            group_num += 1

            cnt = 0
            cur = idx
            while not visited[cur]:
                cnt += 1
                group[cur] = group_num
                visited[cur] = cnt
                cur = preference[cur]
            # 사이클이 형성된 경우 (같은 그룹인 경우)
            if group[cur] == group[idx]:
                # print('cycle', idx, cur)
                # print(group)
                # print(visited)
                left += visited[cur] - 1
                # print(left)
            # 사이클이 형성되지 않은 경우 ( 다른 그룹인 경우)
            else:
                # print('no-cycle', idx, cur)
                # print(group)
                # print(visited)
                left += cnt
                # print(left)

    print(left)