import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N,M = map(int,input().split())
    M_idx = M
    lst = list(map(int,input().split()))
    cnt = 1
    while max(lst) != lst[M_idx]:
        i = 0
        while lst[i] != max(lst):
            print(f'{M = } {lst = }')
            lst.append(lst.pop(i))
            if M <= i:
                M = N-1
            else:
                M -= 1
        lst.pop(i)
        i += 1
    print(M)