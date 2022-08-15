'''
알고리즘을 먼저 만들지 말고,
tc를 분석하고 알고리즘을 만들자.
tc를 직접 그려보자.

다양한 tc를 내가 만들어보자.
내 알고리즘의 빈틈을 찾자.
'''

from collections import deque


T = int(input())
for tc in range(1, T+1):
    N, idx = tuple(map(int, input().split()))
    q = deque(map(int, input().split()))

    cnt = 0
    target = q[idx]

    while q:
        if q[0] == max(q):
            cnt += 1
            if idx == 0:
                break
            q.popleft()

        else:
            q.append(q.popleft())

        idx -= 1
        if idx < 0:
            idx = len(q) - 1

    print(cnt)