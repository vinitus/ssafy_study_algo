# 76ms
string = input()

result = []
stk = []
ref = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

for s in string:
    if s.isalpha():  # 피연산자: push
        result.append(s)

    else:  # 연산자일 경우:
        if s == '(':  # '(': push
            stk.append(s)

        elif s == ')':  # ')': '('만날때까지 stk.pop()
            while stk[-1] != '(':
                result.append(stk.pop())
            stk.pop()  # '('은 버림

        else:  # 그 외 연산자일 경우:
            while stk and ref[s] <= ref[stk[-1]] and stk[-1] != '(':  # 자기보다 우선순위가 낮은 연산자를 만나거나, '('를 만날 때가지 stk.pop()
                result.append(stk.pop())
            stk.append(s)  # 그 다음에 연산자 push

    # print(stk)

while stk:  # 연산이 끝난 후, 남은 연산자들도 모두 결과값으로 stk.pop()
    result.append(stk.pop())

print(''.join(result))
##########################################################################################################################
# 2차 Try 망...
#
# from collections import deque
# input = sys.stdin.readline
#
# fml = input().rstrip()
# ref = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3, ')': 3}
# stk = []
# ans = []
#
# for f in fml:
#     if f.isalpha():
#         ans.append(f)
#     elif f == '(':
#         stk.append(f)
#     elif f== ')':
#         while stk and ref[stk[-1]] < ref[f]:
#             ans.append(stk.pop())
#         stk.append(f)
#     else:
#         while stk and ref[stk[-1]] <= ref[f]:
#             ans.append(stk.pop())
#         stk.append(f)
#
# ans += stk
# ans = ''.join(ans)
# ans = ans.replace('(','')
# ans = ans.replace(')','')
#
# print(ans)

##########################################################################################################################
 # A * ( B + C ) -> ABC+*
 # A B C
 # * ( + )

 # A + ( B + ( C + D ) * E ) -> ABCD+E*+A+
 # A B C D E
 # + ( + ( + ) * )
 # )를 마주하면 저장된 문자는 모두 나감,
 # ( 까지의 연산자 아웃

 # A B C
 # * (

 # A B
 # +

 # A + B * C -> ABC*+
 # A B C
 # + *
 # 우선 순위가 높으면, 들어가기

 # A * B * C + D -> ABC**D+
 # A B C
 # * +
 # 우선 순위가 작으면, 앞에 들어온 문자와 나가기

 # A+B*C*D*E -> ABC*D*E*+
 # A B C D E
 # + * * *
 # 우선 순위가 같으면, 앞에 들어온 문자와 나가기


 # A + B * (C - D / E + F) -> ABCDE/-F+*+
 # A B C D E
 # + * , - /

##############################################################################################################
# 1차 Try
# # 문자는 그대로 deque 집어넣고 -> FIFO 빼기
# # 연산자는 그대로 stack에 집어넣고 -> LIFO 빼기
# fml = ['('] + list(input().rstrip()) + [')']
# ref = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0, ')': 0}
# alQue = deque()
# opStk = []
# parenStk = []
# ans = []
#
# for f in fml:
#     if f.isalpha():                             # f가 문자일 경우
#         alQue.append(f)                             # alpha에 in
#
#     elif f in ['*', '/', '+', '-']:             # f가 연산자일 경우
#         if not opStk or ref[opStk[-1]] < ref[f]:    # 우선순위가 높을 경우
#             opStk.append(f)                         # ope에 in
#         else:                                   # 우선순위가 같거나 낮을 경우
#             while alQue:                            # alpha 모두 append(out)
#                 ans.append(alQue.popleft())
#             while opStk and (opStk[-1] != '(' and ref[opStk[-1]] >= ref[f]):       # ope ( 만나거나 빌 때까지 append(out)
#                 ans.append(opStk.pop())
#             if opStk and opStk[-1] == '(':
#                 opStk.pop()
#             opStk.append(f)                         # ope에 in
#
#     elif f == '(':                              # f가 '('일 경우
#         opStk.append(f)                             # ope에 in
#
#     else:                                       # 연산자가 ')' 일 경우
#         while alQue:                                # alpha 모두 append(out)
#             ans.append(alQue.popleft())
#         while opStk and opStk[-1] != '(':       # ope ( 만나거나 빌 때까지 append(out)
#             ans.append(opStk.pop())
#         if opStk and opStk[-1] == '(':
#             opStk.pop()
# print(opStk)
# print(''.join(ans))