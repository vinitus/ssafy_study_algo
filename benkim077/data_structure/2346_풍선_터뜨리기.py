'''
enumerate를 이용해서 index - value 을 계속 연결시킬 수 있다.

rotate(1)은 시계 방향(오른쪽)으로 1칸, rotate(-1)는 반시계 방향(왼쪽)으로 1칸
'''

from collections import deque


N = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while q:
    idx, value = q.popleft()

    ans.append(idx + 1)

    if value > 0:
        q.rotate(-(value - 1))
    else:
        q.rotate(-value)

print(' '.join(map(str, ans)))