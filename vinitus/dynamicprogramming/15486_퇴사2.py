import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
adj = []
for i in range(N):
    adj.append(tuple(map(int,input().split())))
    
dp = [0 for _ in range(N)]

for i in range(N-1,-1,-1):
    pass