from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
queue = deque()
for _ in range(N):
    input_lst = list(sys.stdin.readline().split())
    if input_lst[0] == 'push':
        queue.append(input_lst[1])
        
    elif input_lst[0] == 'pop':
        if len(queue) < 1:
            print(-1)
        else:
            tmp = queue.popleft()
            print(tmp)
            
    elif input_lst[0] == 'size':
        print(len(queue))
        
    elif input_lst[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
            
    elif input_lst[0] == 'front':
        if len(queue) < 1:
            print(-1)
        else:
            print(queue[0])
            
    elif input_lst[0] == 'back':
        if len(queue) < 1:
            print(-1)
        else:
            print(queue[-1])