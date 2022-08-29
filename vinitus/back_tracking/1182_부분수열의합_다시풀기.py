import sys
def input():
    return sys.stdin.readline().rstrip()

def dfs(n,sm):
    global ans
    if n == N:
        if sm == S:
            ans += 1
        return
    dfs(n + 1, sm+lst[n])
    dfs(n + 1, sm)

N, S = map(int, input().split())
lst = list(map(int,input().split()))
ans = 0

if S == 0:
    ans -= 1

dfs(0,0)

print(ans)