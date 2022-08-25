import sys


def input():
    return sys.stdin.readline().rstrip()


def travel(current, visited, cost, i):
    global min_cost
    if cost >= min_cost:
        return None
    if i == N - 1:
        if trip_map[current][0]:
            cost += trip_map[current][0]
            min_cost = min(cost, min_cost)
        return None
    for k in range(1, N):
        if not visited[k] and trip_map[current][k]:
            tmp = visited[:]
            tmp[k] = True
            travel(k, tmp, cost + trip_map[current][k], i + 1)


min_cost = 1e10
N = int(input())
trip_map = [list(map(int, input().split())) for _ in range(N)]

travel(0, [False] * (N + 1), 0, 0)
print(min_cost)
