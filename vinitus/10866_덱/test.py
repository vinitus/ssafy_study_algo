from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
deq = deque()

for i in range(N):
    order = list(input().split())
    if order[0] == 'push_front':
        deq.appendleft(order[1])
    
    elif order[0] == 'push_back':
        deq.append(order[1])
        
    elif order[0] == 'pop_front':
        if len(deq) < 1:
            print(-1)
        else:
            tmp = deq.popleft()
            print(tmp)
            
    elif order[0] == 'pop_back':
        if len(deq) < 1:
            print(-1)
        else:
            tmp = deq.pop()
            print(tmp)
            
    elif order[0] == 'size':
        print(len(deq))
        
    elif order[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
            
    elif order[0] == 'front':
        if len(deq) < 1:
            print(-1)
        else:
            print(deq[0])
            
    elif order[0] == 'back':
        if len(deq) < 1:
            print(-1)
        else:
            print(deq[-1])