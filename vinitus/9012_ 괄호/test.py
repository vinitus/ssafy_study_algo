T = int(input())

for _ in range(T):
    stack = []
    str_in = input()
    for i in str_in:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')
    