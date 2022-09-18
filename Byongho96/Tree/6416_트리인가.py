# 68ms
import sys
input = sys.stdin.readline

tc = 0
while True:
    tc += 1
    pairs = []
    while True:
        pairs.extend(list(map(int, input().split())))
        if not pairs:
            continue
        if not pairs[-1]:
            pairs.pop()
            pairs.pop()
            break
        if pairs[-1] < 0:
            exit()
    # print('pairs', pairs)

    # 0. 노드가 없어도 트리이다.
    # 1. 루트노드는 부모노드가 없다 V
    # 2. 그 외 노드는 모두 하나의 부모만 가진다 V
    # 3. 모든 노드는 루트로부터터 방문가능하다 V

    # 0. 노드가 없어도 트리이다.
    if not pairs:
        print(f'Case {tc} is a tree.')
        continue

    # 2. 그 외 노드는 모두 하나의 부모만 가진다
    c = 0
    par = [0] * (max(pairs) + 1)
    for i in range(len(pairs) // 2):
        p, c = pairs[2*i], pairs[2*i+1]
        if not par[c]:
            par[c] = p
        else:
            c = -1
            break
    if c < 0:
        print(f'Case {tc} is not a tree.')
        continue

    # print('par', par)

    # 1. 루트노드는 부모노드가 없다 V
    def find_root(c):
        visited = [0] * len(par)
        visited[c] = 1
        while par[c]:
            c = par[c]
            if visited[c]:
                return 0
            visited[c] = 1
        return c
    
    root = find_root(c)
    if not root:
        print(f'Case {tc} is not a tree.')
        continue

    # print('root', root)

    # 3. 모든 노드는 루트로부터터 방문가능하다 V
    def dfs(v):
        global cnt
        visited = [0] * len(par)
        stk = []

        cnt += 1
        visited[v] = 1
        while True:
            # print(stk)
            # print('v', v)
            for w in range(len(par)):
                if par[w] == v and not visited[w]:
                    stk.append(v)
                    v = w
                    cnt += 1
                    visited[v] = 1
                    break
            else:
                if stk:
                    v = stk.pop()
                else:
                    break

    cnt = 0
    dfs(root)
    # print(cnt)
    if cnt != len(pairs) // 2 + 1: # 총 갯수
        print(f'Case {tc} is not a tree.')
        continue

    print(f'Case {tc} is a tree.')