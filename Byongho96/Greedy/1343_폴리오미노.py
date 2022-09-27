# 68ms
import sys
input = sys.stdin.readline

board = input().rstrip().split('.')

result = []
for section in board:
    a, b = divmod(len(section),4)
    if b % 2:
        print(-1)
        break
    result.append('AAAA'*a + 'BB'*(b//2))
else:
    print('.'.join(result))





##################################################

# board = list(input().rstrip())
# N = len(board)
#
# flag = False
# i = 0
# while i < N:
#     if board[i] == '.':
#         i += 1
#     else:
#         if board[i:i + 4] == ['X', 'X', 'X', 'X']:
#             board[i:i + 4] = ['A', 'A', 'A', 'A']
#             i += 4
#         elif board[i:i + 2] == ['X', 'X']:
#             board[i:i + 2] = ['B', 'B']
#             i += 2
#         else:
#             print(-1)
#             flag = True
#             break
#
# if not flag:
#     print(''.join(board))