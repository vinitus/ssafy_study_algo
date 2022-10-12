from collections import deque
import sys
input = sys.stdin.readline

# 1차원 bfs with 딕셔너리 instead of visited array

def bfs(waters):
    dict = {}
    q = deque()
    for water in waters:
        dict[water] = 0
        q.append(water)

    cnt = 0
    result = 0
    while q:
        x = q.popleft()
        # print(x, dict)
        for dx in (-1, 1):
            nx = x + dx
            if nx not in dict:
                dict[nx] = dict[x] + 1
                q.append(nx)
                cnt += 1
                result += dict[nx]
                if cnt == K:
                    return result

N, K = map(int, input().split())
waters = list(map(int, input().split()))

result = bfs(waters)
print(result)

