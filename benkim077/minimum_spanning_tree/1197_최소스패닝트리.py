def find_set(x):
    if tree[x] != x:
        tree[x] = find_set(tree[x])
    return tree[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x < y:
        tree[y] = x
    else:
        tree[x] = y
    

V, E = map(int, input().split())

edge = [0] * E
for i in range(E):
    s, e, w = map(int, input().split())
    edge[i] = (s, e, w)


edge.sort(key=lambda x:x[2])
tree = [i for i in range(0, V + 1)]
total = 0
for s, e, w in edge:
    if find_set(s) != find_set(e):
        union(s, e)
        total += w

print(total)