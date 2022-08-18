# 괄호 유효성 판별함수
def isVPS(parenthesis: str) -> bool:
    stk = [0] * 50
    top = -1
    for p in parenthesis:
        if p == '(':
            top += 1
            stk[top] = p
        else:
            if top != -1 and stk[top] == '(':
                top -= 1
            else:
                return False
    if top != -1:
        return False
    return True

# 메인함수
for T in range(int(input())):
    parenthesis = input()
    result = isVPS(parenthesis)

    if result:
        print('YES')
    else:
        print('NO')