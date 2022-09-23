import sys
def input():
    return sys.stdin.readline().rstrip()
sys.setrecursionlimit()

#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################

N = int(input())
tree = [[] for _ in range(N+1)]
weights = [[] for _ in range(N+1)]
fr = set()
to = set()
for _ in range(N-1):
    parent,child,weight = map(int,input().split())
    fr.add(parent)
    to.add(child)
    tree[parent].append(child)
    tree[child].append(parent)
    weights[parent].append(weight)
    weights[child].append(weight)
candidate = to-fr
if len(tree[1]) == 1:
    candidate.add(1)
list_candidate = list(candidate)
ans = 0



def traverse(num,total):
    visited[num] = True
    if total == 0:
        for i in range(len(tree[num])):
            node = tree[num][i]
            if not visited[node]:
                traverse(node,total+weights[num][i])

    if num in candidate:
        global ans
        if ans < total:
            ans = total
        return None

    for i in range(len(tree[num])):
        node = tree[num][i]
        if not visited[node]:
            traverse(node,total+weights[num][i])
for n in list_candidate:
    visited = [None] * (N + 1)
    traverse(n,0)
    parent = tree[n][0]
    tree[parent].remove(n)
    weights[parent].remove(weights[n][0])
print(ans)