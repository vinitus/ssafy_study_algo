import sys
input = sys.stdin.readline

# # 264 ms
# # num_list 형성
# N = int(input())
# num_list = [0] * N
# for i in range(N):
#     num_list[i] = i+1
# ptrNum = 0
#
# # 데이터 수행
# stk = [0] * (N + 1)
# top = 0
# rlt = []
# flag = True
# for _ in range(N):
#     num = int(input())
#     if num > stk[top]:
#         while ptrNum != N and num_list[ptrNum] <= num:
#             top += 1
#             stk[top] = num_list[ptrNum]
#             ptrNum += 1
#             rlt.append('+')
#         if stk[top] != num:
#             print('NO')
#             break
#         top -= 1
#         rlt.append('-')
#     else:
#         while stk[top] > num:
#             top -= 1
#             rlt.append('-')
#         if stk[top] != num:
#             print('NO')
#             break
#         top -= 1
#         rlt.append('-')
#
# else:
#     for i in rlt:
#         print(i)

## 1. 스택의 특성 상 바로 스택의 윗값과 비교만 하면 된다
## 2. 순서대로 증가하는 리스트의 경우 -> 변수++
N = int(input())
stk = [0] * (N + 1) # 첫번째 값이 0으로 셋팅된 스택
top = 0
cnt = 1
oprLst = []
for _ in range(N):
    num = int(input())
    while num >= cnt:
        top += 1
        stk[top] = cnt
        oprLst.append('+')
        cnt += 1
    if stk[top] == num:
        top -= 1
        oprLst.append('-')
    else:
        print('NO')
        break
else:
    for i in oprLst:
        print(i)

