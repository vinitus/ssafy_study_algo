# Circular Queue 구현 100ms

import sys
input = sys.stdin.readline

class Deque:
    def __init__(self, N):
        self.N = N
        self.dq = [0] * (N + 1)
        self.first = 0
        self.last = 0
    def isEmpty(self):
        if self.first == self.last:
            return True
        return False
    def isFull(self):
        if self.first == (self.last + 1) % (self.N + 1):
            return True
        return False
    def push_front(self, X):
        if self.isFull():
            print('overflow')
            return
        self.dq[self.first] = X
        self.first -= 1
        if self.first == -1:
            self.first = self.N
        return
    def push_back(self, X):
        if self.isFull():
            print('overflow')
            return
        self.last = (self.last + 1) % (self.N + 1)
        self.dq[self.last] = X
        return
    def pop_front(self):
        if self.isEmpty():
            return -1
        self.first = (self.first + 1) % (self.N + 1)
        return self.dq[self.first]
    def pop_back(self):
        if self.isEmpty():
            return -1
        tmp = self.dq[self.last]
        self.last -= 1
        if self.last == -1:
            self.last = self.N
        return tmp
    def size(self):
        if self.last >= self.first:
            return self.last - self.first
        return (self.N + 1 - (self.first - self.last))
    def front(self):
        if self.isEmpty():
            return -1
        return self.dq[(self.first + 1) % (self.N + 1)]
    def back(self):
        if self.isEmpty():
            return -1
        return self.dq[self.last]

N = int(input())
d = Deque(N)
for _ in range(N):
    cmd = input().rstrip()
    if cmd == 'pop_front':
        print(d.pop_front())
    elif cmd == 'pop_back':
        print(d.pop_back())
    elif cmd == 'size':
        print(d.size())
    elif cmd == 'empty':
        print('%d' %d.isEmpty())
    elif cmd == 'front':
        print(d.front())
    elif cmd == 'back':
        print(d.back())
    else:
        cmd = cmd.split()
        if cmd[0][-1] == 'k':
            d.push_back(int(cmd[1]))
        else:
            d.push_front(int(cmd[1]))