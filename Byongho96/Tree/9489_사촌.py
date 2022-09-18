# 1104ms
import sys
input = sys.stdin.readline

while True:
    N, K = map(int, input().split())
    if not N:
        break

    item = list(map(int, input().split()))
    L = len(item)
    par = [-1] * L

    par_ptr = -1
    for i in range(1, L):
        if item[i] > item[i-1] + 1:
            par_ptr += 1
        par[i] = par_ptr

    idx = item.index(K)
    grand_pr = par[par[idx]]
    pr = par[idx]
    cnt = 0
    for i in range(1, N):
        if par[par[i]] == grand_pr and par[i] != pr:
            cnt += 1

    print(cnt)