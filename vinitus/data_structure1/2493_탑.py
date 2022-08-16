import sys

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))
result_lst = [0] * N       
stk = []
for i in range(N-1, -1, -1):
    while stk and lst[stk[-1]] <= lst[i]:
        result_lst[stk.pop()] = i+1
    stk.append(i)

print(' '.join(map(str,result_lst)))

# ' '.join(list) vs *list
# 메모리: 많이, 적게
# 속  도: 빠름, 느림