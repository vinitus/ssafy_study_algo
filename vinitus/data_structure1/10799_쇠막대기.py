lst = list(input())

stk = []
cnt = 0
for i in range(len(lst)):
    if lst[i] == "(":
        stk.append("(")
    else:
        stk.pop()
        if lst[i-1] == "(":
            cnt += len(stk)
        elif lst[i-1] == ")":
            cnt += 1
            
print(cnt)