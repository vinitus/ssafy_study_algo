import sys

sys.setrecursionlimit(200000)
def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################


N, R = map(int, input().split())

if N == 1:
    print("0 0")
    exit()

tree = [[] for _ in range(N + 1)]
weight = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, d = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    weight[a].append(d)
    weight[b].append(d)

# find giganode
gidoong = 0
if N == 2:
    giganode = R
    rt = R
    visited = [None] * (N + 1)
    visited[rt] = True
else:
    rt = R
    if len(tree[rt]) > 1:
        giganode = rt
        visited = [None] * (N + 1)
        visited[rt] = True
    else:
        visited = [None] * (N + 1)
        visited[rt] = True
        gidoong += weight[rt][0]
        rt = tree[rt][0]
        while True:
            visited[rt] = True
            if len(tree[rt]) == 2:
                for i in range(len(tree[rt])):
                    num = tree[rt][i]
                    if not visited[num]:
                        gidoong += weight[rt][i]
                        rt = num
                        break
            elif len(tree[rt]) > 2:
                giganode = rt
                break
            else:
                giganode = rt
                break

max_num = 0


def bfs(rt, num):
    global max_num
    visited[rt] = True
    if len(tree[rt]) == 1:
        max_num = max(num, max_num)
        return None
    for i in range(len(tree[rt])):
        n = tree[rt][i]
        if not visited[n]:
            bfs(n, num + weight[rt][i])


bfs(giganode, 0)
print(gidoong,max_num)
