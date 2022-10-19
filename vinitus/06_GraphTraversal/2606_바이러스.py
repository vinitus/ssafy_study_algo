import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
M = int(input())

computer = list(list() for i in range(N+1))
for i in range(M):
    a,b = map(int,input().split())
    computer[a].append(b)
    computer[b].append(a)

def dfs(n):
    stk = [n]
    visited = [0] * (N+1)
    while stk:
        idx = stk.pop()
        visited[idx] = 1
        for i in computer[idx]:
            if not visited[i]:
                stk.append(i)
                visited[i] = 1
    return sum(visited)

print(dfs(1)-1)