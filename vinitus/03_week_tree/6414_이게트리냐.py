import sys
def input():
    return sys.stdin.readline().rstrip()

llst = []
lst = []
while True:
    tmp = input().split('  ')
    if tmp == ['-1 -1']:
        break
    elif tmp == ['']:
        continue
    elif '0 0' in tmp:
        tmp.pop()
        for i in tmp:
            lst.append(list(map(int, i.split())))
        llst.append(lst)
        lst = []
    else:
        for i in tmp:
            lst.append(list(map(int, i.split())))

for t in range(1,len(llst)+1):
    lst = llst[t-1][:]
    if len(lst) <= 0:
        print(f'Case {t} is a tree.')
        continue
    adj = {}
    sett = set()
    arrive = []
    visited = {}
    for i in lst:
        a,b = i[0], i[1]
        if a in adj:
            adj[a].append(b)
        else:
            adj[a] = [b]
            sett.add(a)
        visited[a] = 0
        visited[b] = 0
        arrive.append(b)
    if len(arrive) != len(set(arrive)):
        print(f'Case {t} is not a tree.')
        continue
    root = []
    for i in sett:
        if i not in arrive:
            root.append(i)
    if not root:
        print(f'Case {t} is not a tree.')
        continue

    if len(root) > 1:
        print(f'Case {t} is not a tree.')
        continue
    i = root[0]
    q = [i]
    visited[i] = 1
    while q:
        idx = q.pop()
        for j in adj[idx]:
            if not visited[j]:
                visited[j] = 1
                if j in sett:
                    q.append(j)

    for k,v in visited.items():
        if v == 0:
            print(f'Case {t} is not a tree.')
            break
    else:
        print(f'Case {t} is a tree.')