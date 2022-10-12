'''
6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8
'''
import sys
input = sys.stdin.readline

def find_set(x):
    if x != tree[x]:
        tree[x] = find_set(tree[x])
    return tree[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x < y:
        tree[y] = x
    else:
        tree[x] = y


N = int(input())
M = int(input())

edge_lst = [0] * M
for i in range(M):
    a, b, c = map(int, input().split())
    edge_lst[i] = (a, b, c)

ans = 0
tree = [i for i in range(N + 1)]
edge_lst.sort(key=lambda x:x[2])
for s, e, w in edge_lst:
    if find_set(s) != find_set(e):
        union(s, e)
        ans += w

print(ans)