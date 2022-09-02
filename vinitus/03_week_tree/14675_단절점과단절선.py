import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lst1 = list(map(int,input().split()) for _ in range(N))

Q = int(input())
lst2 = list(map(int,input().split()) for _ in range(N))