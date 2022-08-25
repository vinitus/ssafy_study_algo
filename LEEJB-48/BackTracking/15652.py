import sys
def input():
    return sys.stdin.readline().rstrip()

def backtracking(current_num,ret):
    if len(ret) == N:
        print(*ret)
        return None
    for i in range(current_num,M+1):
        backtracking(i,ret+[i])
    return None
M,N = map(int,input().split())
backtracking(1,[])