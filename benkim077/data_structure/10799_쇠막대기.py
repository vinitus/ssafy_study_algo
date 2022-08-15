'''
시간초과로 pypy3로 제출
'''

data_lst = list(input())
N = len(data_lst)

lst = [0]*N
cnt = 0
for i in range(N):
    if data_lst[i] == '(':
        cnt += 1
        lst[i] = cnt
    else:
        if data_lst[i - 1] == '(':
            lst[i-1] = lst[i] = -1
            cnt -= 1
        else:
            lst[i] = cnt
            cnt -= 1

ans_lst = []
ans = 0
open = False
for i in range(N):
    if lst[i] == -1:
        if open == True:
            open = False
            ans += len(ans_lst)
        else:
            open = True

    else:
        if lst[i] in ans_lst:
            ans_lst.pop()
            ans += 1
        else:
            ans_lst.append(lst[i])

print(ans)