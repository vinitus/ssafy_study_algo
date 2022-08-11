from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int,input().split())

deq = deque(i for i in range(1,N+1))
result = "<"
while deq:
    deq.rotate(-(K-1))
    result += str(deq.popleft()) + ", "
print(result[:-2]+">")