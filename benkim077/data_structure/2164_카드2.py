from collections import deque
N = int(input())

q = deque(i+1 for i in range(N))

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])