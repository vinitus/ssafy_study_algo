import sys
def input():
    return sys.stdin.readline().rstrip()

def sol(N,K):
    dp = [1] + [0 for _ in range(K)]

    for i in range(N):
        i = int(input())
        for j in range(i, K+1):
            dp[j] += dp[j-i]

    print(dp[-1])
    return

sol(*map(int,input().split()))