import sys
input = sys.stdin.readline

N = int(input())
string = input().rstrip()
numDict = [0] * N
for i in range(N):
    numDict[i] = int(input())

stk = []

for a in string:
    # print(f'a: {a}')
    # print(f'stk: {stk[top]}')
    if a.isalpha():
        a = numDict[ord(a)-ord('A')]
        stk.append(a)
        continue
    B = stk.pop()
    A = stk.pop()
    if a == '*':
        C = A * B
    elif a == '+':
        C = A + B
    elif a == '/':
        C = A / B
    else:
        C = A - B
    stk.append(C)

print('%.2f' %stk[0])
