import sys
input = sys.stdin.readline

# Circular Queue
# 최대 2000000개의 데이터를 저장
# 시간초과는 안나지만, 파이썬의 deque를 쓰는게 더 빠름
class Queue:
    MAX_SIZE = 2000000 + 1
    def __init__(self):
        self.queue = [0] * Queue.MAX_SIZE
        self.first = 0
        self.rear = 0
    def isFull(self):
        if (self.rear + 1) % Queue.MAX_SIZE == self.rear:
            return True
        return False
    def isEmpty(self):
        if self.first == self.rear:
            return True
        return False
    def push(self, X):
        if self.isFull():
            print('over flow')
            return
        self.rear = (self.rear + 1) % Queue.MAX_SIZE
        self.queue[self.rear] = X
    def pop(self):
        if self.isEmpty():
            return -1
        self.first = (self.first + 1) % Queue.MAX_SIZE
        return self.queue[self.first]
    def size(self):
        # print(f'first: {self.first}. rear: {self.rear}')
        if self.rear >= self.first:
            return self.rear - self.first
        return (Queue.MAX_SIZE - (self.first - self.rear))
    def front(self):
        if self.isEmpty():
            return -1
        return self.queue[(self.first + 1) % Queue.MAX_SIZE]
    def back(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

queue = Queue()
for _ in range(int(input())):
    cmd = input().rstrip()
    if cmd == 'pop':
        print(queue.pop())
    elif cmd == 'size':
        print(queue.size())
    elif cmd == 'empty':
        print('%d' %queue.isEmpty())
    elif cmd == 'front':
        print(queue.front())
    elif cmd == 'back':
        print(queue.back())
    else:
        X = int(cmd.split()[1])
        queue.push(X)