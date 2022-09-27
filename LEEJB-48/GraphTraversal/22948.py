import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################

N = int(input())

array = []
graph = [[] for _ in range(N + 1)]

for _ in range(N):
    num, mid, r = map(int, input().split())
    array.append((num, mid - r))
    array.append((num, mid + r))
start, end = map(int, input().split())
array.sort(key=lambda x: x[1])
stack = [0]
array.append((0, array[-1][1] + 1))

for num, _ in array:
    if stack[-1] != num:
        graph[num].append(stack[-1])
        graph[stack[-1]].append(num)
        stack.append(num)
    else:
        stack.pop()
visited = [False] * (N + 1)
del array, stack


def bfs(node):
    queue = deque()
    queue.append([node])
    while queue:
        tmp_queue = deque()
        for _ in range(len(queue)):
            cur = queue.popleft()
            last = cur[-1]
            if last == end:
                return cur
            for num in graph[last]:
                if not visited[num]:
                    visited[num] = True
                    tmp_queue.append(cur + [num])
        queue = tmp_queue
    return None


ans = bfs(start)
print(len(ans))
print(' '.join(map(str, ans)))
