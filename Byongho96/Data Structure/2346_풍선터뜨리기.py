# 포인터를 옮기면서 pop하는게 deque 로테이트 후 pop보다 빠름
# 68ms 92ms
import sys
input = sys.stdin.readline

ptr = 0
N = int(input())
balloons = list(enumerate(map(int, input().split())))
lst = []

for _ in range(N-1):
    K = balloons[ptr][1]
    i = balloons[ptr][0]
    balloons.pop(ptr)
    lst.append(i+1)
    if K > 0:
        ptr = (ptr + K - 1) % len(balloons)
    else:
        ptr = (ptr + K) % len(balloons)
lst.append(balloons[ptr][0] + 1)

print(*lst)