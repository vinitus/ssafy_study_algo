import sys

input = sys.stdin.readline

N = int(input())

lst = list(input())
lst.pop()
order = ['+','-','*','/']
stk_num = []
for i in range(len(lst)):
    if lst[i].isdigit():
        stk_num.append(int(lst[i]))
    elif lst[i] not in order:
        tmp = int(input())
        stk_num.append(tmp)
        for j in range(i+1, len(lst)):
            if lst[j] == lst[i]:
                lst[j] = str(tmp)
    else:
        if lst[i] == "+":
            stk_num.append(stk_num.pop(-2) + stk_num.pop())
        elif lst[i] == "-":
            stk_num.append(stk_num.pop(-2) - stk_num.pop())
        elif lst[i] == "*":
            stk_num.append(stk_num.pop(-2) * stk_num.pop())
        else:
            stk_num.append(stk_num.pop(-2) / stk_num.pop())

print(f'{stk_num[0]:.02f}')