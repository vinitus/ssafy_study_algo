## 548ms

import sys
input = sys.stdin.readline

N = int(input())
points = []
stk = []

for i in range(N):
    cen, rad = map(int, input().split())
    points.append((cen - rad, 0, i))    # 여는괄호
    points.append((cen + rad, 1, i))    # 닫는 괄호

points.sort(key=lambda x: x[0])

for point in points:
    if point[1] == 0:
        stk.append(point)
    else:
        if stk and stk[-1][2] == point[2]:
            stk.pop()
        else:
            print('NO')
            break
else:
    if not stk:
        print('YES')
    else:
        print('NO')

