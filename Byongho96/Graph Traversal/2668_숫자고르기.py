import sys
input = sys.stdin.readline

# 사이클 찾기. DFS, BFS도 아니고 그냥 열심히 찾기

N = int(input())
nums = [0] * (N + 1)
for i in range(1, N + 1):
    nums[i] = int(input())

cycle = []
visited = [0] * (N + 1)
for i in range(1, N + 1):
    if not visited[i]:
        cur = i
        visited[cur] = 1
        path = [cur]
        while nums[cur] not in path and not visited[nums[cur]]:
            cur = nums[cur]
            visited[cur] = 1
            path.append(cur)
        if nums[cur] in path:
            idx = path.index(nums[cur])
            cycle.extend(path[idx:])
print(len(cycle))
cycle.sort()
print('\n'.join(map(str, cycle)))
