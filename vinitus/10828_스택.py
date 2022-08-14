import sys

N = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(N):
    input_lst = list(sys.stdin.readline().split())
    if input_lst[0] == 'push':
        stack.append(input_lst[1])
    elif input_lst[0] == 'pop':
        if len(stack) < 1:
            print(-1)
        else:
            tmp = stack.pop()
            print(tmp)
    elif input_lst[0] == 'size':
        print(len(stack))
    elif input_lst[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif input_lst[0] == 'top':
        if len(stack) < 1:
            print(-1)
        else:
            print(stack[-1])