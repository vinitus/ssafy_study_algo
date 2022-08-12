import sys

input = sys.stdin.readline
N = int(input())
balloon = list(i for i in range(1,N+1))
lst = list(map(int,input().split()))
idx = 0
idx_lst = []
for i in lst:
    idx_lst.append(balloon[idx])
    new_idx = idx + lst[idx]
    while new_idx >= len(balloon)-1:
        new_idx -= len(balloon)-1
    balloon.pop(idx)

    idx = new_idx
print(*idx_lst)