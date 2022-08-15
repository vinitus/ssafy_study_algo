N = int(input())

goal = [int(input()) for _ in range(N)]  
lst = []
ans_lst = []
ans = []


j = 0
for i in range(len(goal)):
    while True: 
        # print(f'j = {j}')
        if j + 1 < goal[i]:
            lst.append(j + 1)
            ans.append('+')
            j += 1
        elif j + 1 == goal[i]:
            lst.append(j + 1)
            ans.append('+')
            j += 1
            ans_lst.append(lst.pop())
            ans.append('-')
            break
        elif j + 1 > goal[i]:
            ans_lst.append(lst.pop())
            ans.append('-')
            break

if ans_lst == goal:
    print('\n'.join(map(str, ans)))
else:
    print('NO')
