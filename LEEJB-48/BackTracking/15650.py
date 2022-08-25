import sys

def input():
    return sys.stdin.readline().rstrip()

def backtracking(i,lst):
    if len(lst) == M:
        print(*lst)
        return None
    if i>N:
        return None
    backtracking(i + 1, lst + [i])
    backtracking(i+1,lst)


N,M = map(int,input().split())
backtracking(1,[])

