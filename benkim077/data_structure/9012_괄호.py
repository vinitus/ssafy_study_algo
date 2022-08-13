T = int(input())

for tc in range(1, T+1):
    lst = list(input())
    info = []

    for i in range(len(lst)):
        info.append(lst[i])
        if len(info) > 1:
            if info[-2] == '(' and info[-1] == ')':
                info.pop()
                info.pop()

    ans = ''
    if len(info) == 0:
        ans = 'YES'
    else:
        ans = 'NO'

    print(ans)
