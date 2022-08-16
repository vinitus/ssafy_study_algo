lst = list(input())
stk = []
result = 0
tmp = 1

for idx in range(len(lst)):
    if lst[idx]== "(":
        stk.append(lst[idx])
        tmp *= 2
    elif lst[idx]== "[":
        stk.append(lst[idx])
        tmp *= 3
    elif lst[idx]== ")":
        if not stk or stk[-1] == "[":
            result = 0
            break
        else:
            if lst[idx-1] == "(":
                result += tmp
                tmp //= 2
                stk.pop()
            else:
                tmp //= 2
                stk.pop()
    elif lst[idx]== "]":
        if not stk or stk[-1] == "(":
            result = 0
            break
        else:
            if lst[idx-1] == "[":
                result += tmp
                tmp //= 3
                stk.pop()
            else:
                tmp //= 3
                stk.pop()
if stk:
    print(0)
else:
    print(result)