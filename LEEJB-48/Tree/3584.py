import sys
def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################
def find_depth(rt):
    stack = [rt]
    dpt = 1
    depth[rt] = 1
    while stack:
        dpt += 1
        tmp_stack = []
        for i in stack:
            for num in tree[i]:
                depth[num] = dpt
                tmp_stack.append(num)
        stack = tmp_stack[:]



T = int(input())
for test_case in range(T):
    N = int(input())
    tree = [[]for _ in range(N+1)]
    ancestor = [None] * (N+1)
    fr = set()
    to = set()
    for _ in range(N-1):
        p,c = map(int,input().split())
        fr.add(p)
        to.add(c)
        tree[p].append(c)
        ancestor[c] = p
    a,b = map(int,input().split())
    root = list(fr-to)[0]
    del fr
    del to
    depth = [None]*(N+1)
    find_depth(root)
    a_depth = depth[a]
    b_depth = depth[b]
    if a_depth > b_depth:
        while(a_depth != b_depth):
            a_depth -= 1
            a = ancestor[a]
    elif b_depth > a_depth:
        while (a_depth != b_depth):
            b_depth -= 1
            b = ancestor[b]
    while (a!=b):
        a = ancestor[a]
        b = ancestor[b]
    print(a)