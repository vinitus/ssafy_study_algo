import collections
import sys


def input():
    return sys.stdin.readline().rstrip()

q = collections.deque()

N = int(input())
for _ in range(N):
    cmd = input()

    if cmd[0:4] == 'push':
        q.append(int(cmd[5:]))
    elif cmd == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif cmd == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
