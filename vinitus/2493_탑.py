import sys

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))
lst_idx = [0] * N
stk = [N-1]
for i in range(N-2, -1, -1):
    while stk and lst[stk[-1]] <= lst[i]:
        lst_idx[stk.pop()] = i+1
    stk.append(i)

print(' '.join(map(str,lst_idx)))