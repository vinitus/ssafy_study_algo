# 100ms
import sys
input = sys.stdin.readline

def find_ancestors(cur):
    ancestors = [cur]
    while cur != 0:
        cur = par[cur]
        ancestors.append(cur)
    return ancestors

T = int(input())

for _ in range(T):
    N = int(input())
    par = [0] * (N + 1)

    for _ in range(N - 1):
        p, c = map(int, input().split())
        par[c] = p

    leaf1, leaf2 = map(int, input().split())
    a1 = find_ancestors(leaf1)
    a2 = find_ancestors(leaf2)
    for a in a1:
        if a in a2:
            print(a)
            break