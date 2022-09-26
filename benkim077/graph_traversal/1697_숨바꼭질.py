# 1차원 bfs라 생각해야하나?
from collections import deque


def bfs():
    q = deque([N])
    vsted[N] = 1

    while q:
        i = q.popleft()
        
        if 0 <= 2 * i < 100_001 and not vsted[2 * i]:
            vsted[2 * i] = vsted[i] + 1
            q.append(2 * i)
        
        if 0 <= i - 1 < 100_001 and not vsted[i - 1]:
            vsted[i - 1] = vsted[i] + 1
            q.append(i - 1)
        
        if 0 <= i + 1 < 100_001 and not vsted[i + 1]:
            vsted[i + 1] = vsted[i] + 1
            q.append(i + 1)
        

N, K = map(int, input().split())
vsted = [0] * 100_001   # 0 ~ 100_000번 인덱스

bfs()
print(vsted[K] - 1)
