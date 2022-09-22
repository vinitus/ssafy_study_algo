import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################
N, K = map(int, input().split())
if K <= N:
    print(N - K)
else:
    visited = [False] * (K + 1)
    queue = deque()
    queue.append(N)

    ans = K - N
    cnt = 0
    while True:
        # 먼저 곱하기를 다 해준다
        for _ in range(len(queue)):
            cur = queue.popleft()
            if cur == K:
                ans = min(ans, cnt + cur - K)
                break
            visited[cur] = False
            while True:
                if visited[cur]:
                    break
                visited[cur] = True
                queue.append(cur)
                cur = cur * 2
                if cur >= K:
                    ans = min(ans, cnt + cur - K)
                    break
        if cnt >= ans:
            break
        # 이제 다 처리해준다
        for _ in range(len(queue)):
            cur = queue.popleft()

            if cur >= 1 and not visited[cur - 1]:
                visited[cur - 1] = True
                queue.append(cur - 1)
            if cur + 1 <= K and not visited[cur + 1]:
                visited[cur + 1] = True
                queue.append(cur + 1)
        cnt += 1
    print(ans)
