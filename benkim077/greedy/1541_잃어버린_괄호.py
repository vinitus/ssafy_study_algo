# 입력(숫자)를 처리하자
# 괄호는 그냥 처리 안해도 되겠는데?
import sys
sys.stdin = open('input.txt')


data = input()

lst = []
temp = ''
for char in data:
    if char.isnumeric():
        temp += char
    else:
        lst.append(temp)
        temp = ''
        lst.append(char)
else:
    lst.append(temp)

ans = 0
operator = '+'
for element in lst:
    if element.isnumeric():
        if operator == '+':
            ans += int(element)
        else:
            ans -= int(element)
    else:
        if element == '-':
            operator = element
        else:
            pass

print(ans)