import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
adj = []
for i in range(N):
    adj.append(tuple(map(int,input().split())))
    
dp = [0 for _ in range(N)]

for idx,info in enumerate(adj):
    day,earn = info
    if idx+day < N:
        for i in range(idx,N):
            dp[i] = max(dp[i],earn)

    print(dp)