import sys

input = sys.stdin.readline

def find_parent(a, b):
    a_parent = [a]
    while tree[a]:
        a = tree[a]
        a_parent.append(a)

    if b in a_parent:
        return b

    while tree[b]:
        b = tree[b]
        if b in a_parent:
            return b


T = int(input())
for _ in range(T):
    N = int(input())
    tree = [0] * (N+1)
    for __ in range(N-1):
        p, c = map(int, input().split())
        tree[c] = p
    a, b = map(int, input().split())
    print(find_parent(a, b))
