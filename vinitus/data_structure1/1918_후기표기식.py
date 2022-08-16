lst = list(input())
stk = []
order = ["+","-","*","/"]
brac_lst = ["(",")"]
bracket = []
result = ''
pass_flag = False

for idx in range(len(lst)):
    if pass_flag:
        result += lst[idx]
        while stk:
            result += stk.pop()
        pass_flag = False
        continue
    elif lst[idx] not in order and lst[idx] not in brac_lst:
        result += lst[idx]
    elif lst[idx] in order:
        if lst[idx] == "+" or lst[idx] == "-":
            stk.append(lst[idx])
        else:
            stk.append(lst[idx])
            if not bracket:
                pass_flag = True
    elif lst[idx] == "(":
        bracket.append("(")
    elif lst[idx] == ")":
        bracket.pop()
        while stk:
            result += stk.pop()
while stk:
    result += stk.pop()
print(result)