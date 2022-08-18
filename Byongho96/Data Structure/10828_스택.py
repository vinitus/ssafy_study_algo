import sys
input = sys.stdin.readline

# 스택 클래스
# top 변수(포인터)를 두고, 증감하는 것이 append나 pop보다 빠르다
class Stack:
    def __init__(self):
        self.stk = [0] * 10000
        self.top = -1
        return
    def push(self, X):
        self.top += 1
        self.stk[self.top] = X
        return
    def pop(self):
        if self.top != -1:
            self.top -= 1
            return self.stk[self.top+1]
        return -1
    def size(self):
        print(self.top+1)
        return
    def empty(self):
        if self.top != -1:
            print(0)
            return
        print(1)
        return
    def Top(self):
        if self.top != -1:
            print(self.stk[self.top])
            return
        print(self.top)
        return

stack = Stack()
for _ in range(int(input())):
    cmd = input().rstrip()
    if cmd == 'pop':
        print(stack.pop())
    elif cmd == 'size':
        stack.size()
    elif cmd == 'empty':
        stack.empty()
    elif cmd == 'top':
        stack.Top()
    else:
        X = int(cmd.split()[1])
        stack.push(X)
