import sys
input = sys.stdin.readline

# 직관적이지만, 조건문과 반복문이 여러번 겹침// 68ms
# paren = input().rstrip()
# stk = []
# ref = {')': ('(', 2), ']': ('[', 3)}
#
# flag = 0
# for p in paren:
#     if p == '(' or p == '[':
#         stk.append(p)
#     else:
#         tmp = 0
#         while True:
#             if stk: # 있으면 pop
#                 s = stk.pop()
#                 if isinstance(s, int):    # 숫자면
#                     tmp += s
#                 elif s == ref[p][0]: # 대응 문자면
#                     stk.append(ref[p][1] * (1 if not tmp else tmp))
#                     break
#                 else:
#                     print(0)
#                     flag =1
#                     break
#             else:# 없으면
#                 print(0)
#                 flag = 1
#                 break
#         if flag:
#             break
#
# else:
#     try:
#         print(sum(stk))
#     except:
#         print(0)

# 스택
# 일차원 단방향, 여러 요소, 짝을 짓는다(변형가능) 72ms
paren = input().rstrip()
stk = []
ref = {'(': 2, '[': 3, ')': ('(', 2), ']': ('[', 3)}
ans = 0
tmp = 1

pre = ''
for p in paren:
    if p == '(' or p == '[':
        stk.append(p)
        tmp *= ref[p]
    else:
        if not stk or stk[-1] != ref[p][0]:
            ans = 0
            break
        if pre == ref[p][0]:
            ans += tmp
        tmp //= ref[p][1]
        stk.pop()
    pre = p
if stk:
    print(0)
else:
    print(ans)

